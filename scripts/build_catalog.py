#!/usr/bin/env python3
"""Build a browsable Markdown catalog of the ComfyUI workflow templates.

Reads a (sparse, blobless) clone of Comfy-Org/workflow_templates and writes:

  README.md                      landing page with stats + category overview
  catalog/all.md                 every template in one table
  catalog/newest.md              every template, newest first
  catalog/by-model.md            templates grouped by model family
  catalog/by-tag.md              templates grouped by tag
  catalog/custom-nodes.md        templates grouped by required custom node pack
  catalog/model-files.md         every downloadable model file + who uses it
  catalog/templates.json         machine-readable summary of everything
  catalog/<category>/README.md   thumbnail gallery for one category
  catalog/<category>/<name>.md   detail page for one template

Only the standard library is used. Output is deterministic (no timestamps),
so re-running against an unchanged upstream produces no diff.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ASSET_RE = re.compile(r"^(?P<name>.+)-(?P<n>\d+)\.(?P<ext>webp|png|jpe?g|gif|mp3|mp4|webm)$", re.I)
IMAGE_EXTS = {"webp", "png", "jpg", "jpeg", "gif"}
UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
NOTE_TYPES = {"Note", "MarkdownNote"}


# --------------------------------------------------------------------------- helpers

def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "misc"


def cell(value) -> str:
    """Make a value safe for a single Markdown table cell."""
    if value is None:
        return ""
    s = str(value).replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return re.sub(r"\s+", " ", s).strip()


def human_size(n) -> str:
    if not isinstance(n, (int, float)) or n <= 0:
        return ""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{int(n)} B"
        n /= 1024
    return ""


def git(upstream: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(upstream), *args], check=True, capture_output=True, text=True, encoding="utf-8"
    ).stdout


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------- extraction

OUTPUT_PRIORITY = ["3d", "video", "audio", "image", "text"]


def output_type(t: dict, category_type: str) -> str:
    """What the workflow produces. Upstream `mediaType` describes the thumbnail, not the output."""
    outs = {o.get("mediaType") for o in (t.get("io") or {}).get("outputs") or [] if o.get("mediaType")}
    for kind in OUTPUT_PRIORITY:
        if kind in outs:
            return kind
    return category_type or t.get("mediaType") or "other"


def list_template_files(upstream: Path) -> list[str]:
    """Filenames in templates/ — from git trees, so blobs (images) need not be downloaded."""
    try:
        out = git(upstream, "ls-tree", "--name-only", "HEAD", "templates/")
        return sorted(Path(p).name for p in out.splitlines())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return sorted(p.name for p in (upstream / "templates").iterdir())


def upstream_commit(upstream: Path) -> tuple[str, str]:
    try:
        sha, date = git(upstream, "log", "-1", "--format=%H %cI").split()
        return sha, date
    except Exception:
        return "", ""


def analyze_workflow(path: Path) -> dict:
    """Pull node types, model downloads, custom node packs, subgraphs and notes out of a workflow."""
    info = {
        "node_count": 0,
        "node_types": collections.Counter(),
        "node_packs": {},
        "models": [],
        "custom_nodes": set(),
        "subgraphs": [],
        "notes": [],
        "error": None,
    }
    try:
        wf = load_json(path)
    except Exception as e:  # noqa: BLE001
        info["error"] = f"{type(e).__name__}: {e}"
        return info
    if not isinstance(wf, dict) or "nodes" not in wf:
        info["error"] = "not a workflow file"
        return info

    subgraphs = (wf.get("definitions") or {}).get("subgraphs") or []
    sg_names = {sg.get("id"): sg.get("name") or sg.get("id") for sg in subgraphs}
    info["subgraphs"] = [
        {"name": sg.get("name") or sg.get("id"), "nodes": len(sg.get("nodes") or [])} for sg in subgraphs
    ]

    seen_models = set()
    all_nodes = [(n, False) for n in wf.get("nodes") or []]
    for sg in subgraphs:
        all_nodes += [(n, True) for n in sg.get("nodes") or []]

    for node, _in_subgraph in all_nodes:
        ntype = node.get("type") or "?"
        props = node.get("properties") or {}
        if ntype in sg_names or UUID_RE.match(ntype):
            continue  # subgraph instance, listed separately
        info["node_count"] += 1
        info["node_types"][ntype] += 1
        pack = props.get("cnr_id") or props.get("aux_id")
        if pack:
            info["node_packs"].setdefault(ntype, pack)
            if pack != "comfy-core":
                info["custom_nodes"].add(pack)
        for m in props.get("models") or []:
            key = (m.get("name"), m.get("url"), m.get("directory"))
            if key not in seen_models and m.get("name"):
                seen_models.add(key)
                info["models"].append({"name": m.get("name"), "directory": m.get("directory") or "", "url": m.get("url") or ""})
        if ntype in NOTE_TYPES:
            text = (node.get("widgets_values") or [""])[0]
            if isinstance(text, str) and text.strip():
                info["notes"].append({"type": ntype, "title": node.get("title") or ntype, "text": text.strip()})

    info["models"].sort(key=lambda m: (m["directory"], m["name"].lower()))
    return info


# --------------------------------------------------------------------------- rendering

class Catalog:
    def __init__(self, upstream: Path, out: Path, repo: str, ref: str, site_url: str = ""):
        self.site_url = site_url.rstrip("/") + "/" if site_url else ""
        self.upstream = upstream
        self.out = out
        self.catalog_dir = out / "catalog"
        self.repo = repo
        self.ref = ref
        self.raw = f"https://raw.githubusercontent.com/{repo}/{ref}/templates"
        self.blob = f"https://github.com/{repo}/blob/{ref}/templates"
        self.sha, self.commit_date = upstream_commit(upstream)

        index = load_json(upstream / "templates" / "index.json")
        files = list_template_files(upstream)
        self.file_count = len(files)
        self.assets: dict[str, list[tuple[int, str]]] = collections.defaultdict(list)
        for f in files:
            m = ASSET_RE.match(f)
            if m:
                self.assets[m["name"]].append((int(m["n"]), f))
        json_files = {f[:-5] for f in files if f.endswith(".json") and not f.startswith("index")}

        self.categories = []  # [{title, group, slug, type, templates: [t...]}]
        self.templates = []  # flat list
        used_slugs = set()
        for cat in index:
            slug = slugify(cat.get("title") or cat.get("moduleName") or "misc")
            while slug in used_slugs:
                slug += "-2"
            used_slugs.add(slug)
            c = {
                "title": cat.get("title") or slug,
                "group": cat.get("category") or "",
                "slug": slug,
                "type": cat.get("type") or "",
                "templates": [],
            }
            for t in cat.get("templates") or []:
                t = dict(t)
                t["_category"] = c
                t["_output"] = output_type(t, c["type"])
                t["_page"] = f"{slug}/{t['name']}.md"
                path = upstream / "templates" / f"{t['name']}.json"
                t["_has_json"] = t["name"] in json_files and path.exists()
                t["_wf"] = analyze_workflow(path) if t["_has_json"] else None
                c["templates"].append(t)
                self.templates.append(t)
            self.categories.append(c)

        indexed = {t["name"] for t in self.templates}
        self.unindexed = sorted(
            n for n in json_files - indexed
            if isinstance(self._safe_load(upstream / "templates" / f"{n}.json"), dict)
            and "nodes" in self._safe_load(upstream / "templates" / f"{n}.json")
        )

    @staticmethod
    def _safe_load(path: Path):
        try:
            return load_json(path)
        except Exception:  # noqa: BLE001
            return None

    # ---- small render helpers

    def link(self, t, from_dir: str) -> str:
        """Relative link to a template page from a directory ('' = catalog root, 'cat' = category dir, '..' = repo root)."""
        if from_dir == "root":
            return f"catalog/{t['_page']}"
        if from_dir == "catalog":
            return t["_page"]
        # from inside a category dir
        if t["_category"]["slug"] == from_dir:
            return f"{t['name']}.md"
        return f"../{t['_page']}"

    def thumbs(self, t) -> list[str]:
        return [f for _, f in sorted(self.assets.get(t["name"], []))]

    def thumb_html(self, t, width: int) -> str:
        for f in self.thumbs(t):
            if f.rsplit(".", 1)[-1].lower() in IMAGE_EXTS:
                return f'<img src="{self.raw}/{f}" width="{width}" alt="{cell(t.get("title"))}">'
        for f in self.thumbs(t):
            return f"[▶ preview]({self.raw}/{f})"
        return ""

    @staticmethod
    def kind(t) -> str:
        return "open source" if t.get("openSource", True) else "API"

    def source_line(self) -> str:
        if self.sha:
            return (
                f"Generated from [`{self.repo}@{self.sha[:7]}`](https://github.com/{self.repo}/tree/{self.sha}/templates)"
                f" (upstream commit {self.commit_date[:10]})."
            )
        return f"Generated from [`{self.repo}`](https://github.com/{self.repo}/tree/{self.ref}/templates)."

    def template_row(self, t, from_dir: str, extra_cols=()) -> str:
        cols = [
            f"[{cell(t.get('title') or t['name'])}]({self.link(t, from_dir)})",
            cell(t["_category"]["title"]),
            cell(t["_output"]),
            cell(", ".join(t.get("models") or [])),
            cell(", ".join(t.get("tags") or [])),
            cell(t.get("date")),
            self.kind(t),
        ]
        return "| " + " | ".join(cols + list(extra_cols)) + " |"

    TEMPLATE_HEADER = "| Template | Category | Output | Models | Tags | Date | Type |\n|---|---|---|---|---|---|---|"

    # ---- pages

    def render_template(self, t) -> str:
        c = t["_category"]
        wf = t["_wf"] or {}
        name = t["name"]
        L = [f"# {t.get('title') or name}", ""]
        nav = f"[← {c['title']}](README.md) · [All categories](../README.md) · [All templates](../all.md)"
        if self.site_url:
            nav += f" · [Open in browser]({self.site_url}#t={name})"
        L += [nav, ""]

        imgs = []
        for f in self.thumbs(t):
            ext = f.rsplit(".", 1)[-1].lower()
            if ext in IMAGE_EXTS:
                imgs.append(f'<img src="{self.raw}/{f}" width="360" alt="{cell(t.get("title"))} {f}">')
            else:
                imgs.append(f"[▶ {f}]({self.raw}/{f})")
        if imgs:
            L += [" ".join(imgs), ""]

        if t.get("description"):
            L += ["> " + t["description"].strip().replace("\n", "\n> "), ""]

        L += ["## Get the workflow", ""]
        if t["_has_json"]:
            L += [
                f"- **[Download JSON]({self.raw}/{name}.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).",
                f"- [View on GitHub]({self.blob}/{name}.json)",
            ]
        else:
            L += ["- *Workflow JSON is not present upstream.*"]
        if t.get("tutorialUrl"):
            L += [f"- [Tutorial]({t['tutorialUrl']})"]
        L += [""]

        rows = [
            ("Name", f"`{name}`"),
            ("Category", f"{c['group']} › {c['title']}" if c["group"] else c["title"]),
            ("Output", t["_output"]),
            ("Models", ", ".join(t.get("models") or [])),
            ("Tags", ", ".join(t.get("tags") or [])),
            ("Type", self.kind(t)),
            ("Date", t.get("date")),
            ("Author", t.get("username")),
            ("Download size", human_size(t.get("size"))),
            ("Min ComfyUI version", t.get("minComfyUIVersion")),
            ("Distributions", ", ".join(t.get("includeOnDistributions") or [])),
            ("Usage", t.get("usage")),
            ("Nodes", wf.get("node_count") if t["_has_json"] else None),
        ]
        L += ["## Details", "", "| | |", "|---|---|"]
        L += [f"| {k} | {cell(v)} |" for k, v in rows if v not in (None, "", [])]
        L += [""]

        io = t.get("io") or {}
        if io.get("inputs") or io.get("outputs"):
            L += ["## Inputs & outputs", "", "| Direction | Node | Media | File |", "|---|---|---|---|"]
            for direction in ("inputs", "outputs"):
                for item in io.get(direction) or []:
                    L.append(
                        f"| {direction[:-1]} | `{cell(item.get('nodeType'))}` #{cell(item.get('nodeId'))} "
                        f"| {cell(item.get('mediaType'))} | {cell(item.get('file'))} |"
                    )
            L += [""]

        packs = sorted(set(t.get("requiresCustomNodes") or []) | set(wf.get("custom_nodes") or []), key=lambda s: (s.lower(), s))
        if packs:
            L += ["## Custom nodes required", ""]
            L += [f"- [{p}](https://registry.comfy.org/nodes/{p})" for p in packs]
            L += [""]

        if wf.get("models"):
            L += ["## Model files", "", "| File | Folder (`ComfyUI/models/…`) | Download |", "|---|---|---|"]
            for m in wf["models"]:
                dl = f"[link]({m['url']})" if m["url"] else ""
                L.append(f"| `{cell(m['name'])}` | `{cell(m['directory'])}` | {dl} |")
            L += [""]

        if wf.get("subgraphs"):
            L += ["## Subgraphs", ""]
            L += [f"- **{cell(s['name'])}** ({s['nodes']} nodes)" for s in wf["subgraphs"]]
            L += [""]

        if wf.get("node_types"):
            L += ["## Nodes used", "", "| Node | Count | Pack |", "|---|---|---|"]
            for ntype, n in sorted(wf["node_types"].items(), key=lambda kv: (-kv[1], kv[0].lower())):
                L.append(f"| `{cell(ntype)}` | {n} | {cell(wf['node_packs'].get(ntype, ''))} |")
            L += [""]

        if wf.get("notes"):
            L += ["## Notes embedded in the workflow", ""]
            for note in wf["notes"]:
                L += [f"<details><summary>{cell(note['title'])}</summary>", ""]
                if note["type"] == "MarkdownNote":
                    L += [note["text"]]
                else:
                    L += ["```text", note["text"].replace("```", "ʼʼʼ"), "```"]
                L += ["", "</details>", ""]

        if wf.get("error"):
            L += [f"*Could not parse workflow JSON: {cell(wf['error'])}*", ""]
        return "\n".join(L)

    def render_category(self, c) -> str:
        L = [f"# {c['title']}", ""]
        L += [f"[← All categories](../README.md) · [All templates](../all.md)", ""]
        L += [f"{len(c['templates'])} templates" + (f" · {c['group']}" if c["group"] else "") + ".", ""]
        L += ["| Preview | Template | Models | Date |", "|---|---|---|---|"]
        for t in c["templates"]:
            title = f"**[{cell(t.get('title') or t['name'])}]({t['name']}.md)**"
            desc = cell(t.get("description"))
            meta = " · ".join(x for x in [cell(t["_output"]), self.kind(t), human_size(t.get("size"))] if x)
            L.append(
                f"| {self.thumb_html(t, 200)} | {title}<br>{desc}<br><sub>{meta}</sub> "
                f"| {cell(', '.join(t.get('models') or []))} | {cell(t.get('date'))} |"
            )
        return "\n".join(L)

    def render_catalog_index(self) -> str:
        L = ["# ComfyUI workflow template catalog", "", self.source_line(), ""]
        L += self.category_table("catalog")
        L += self.index_links("catalog")
        return "\n".join(L)

    def category_table(self, from_dir: str) -> list[str]:
        prefix = "catalog/" if from_dir == "root" else ""
        if from_dir == "root":
            L = ["## Categories", "", "| Group | Category | Templates | Output | Gallery |", "|---|---|---|---|---|"]
            for c in self.categories:
                L.append(
                    f"| {cell(c['group'])} | [{cell(c['title'])}](#dir-{c['slug']}) | {len(c['templates'])} "
                    f"| {cell(c['type'])} | [thumbnails]({prefix}{c['slug']}/README.md) |"
                )
            return L + [""]
        L = ["## Categories", "", "| Group | Category | Templates | Output |", "|---|---|---|---|"]
        for c in self.categories:
            L.append(f"| {cell(c['group'])} | [{cell(c['title'])}]({prefix}{c['slug']}/README.md) | {len(c['templates'])} | {cell(c['type'])} |")
        return L + [""]

    def index_links(self, from_dir: str) -> list[str]:
        p = "catalog/" if from_dir == "root" else ""
        return [
            "## Indexes",
            "",
            f"- [All templates (A–Z)]({p}all.md)",
            f"- [Newest first]({p}newest.md)",
            f"- [By model]({p}by-model.md)",
            f"- [By tag]({p}by-tag.md)",
            f"- [By custom node pack]({p}custom-nodes.md)",
            f"- [Model files & download links]({p}model-files.md)",
            f"- [Machine-readable JSON]({p}templates.json)",
            "",
        ]

    def render_flat(self, title: str, templates) -> str:
        L = [f"# {title}", "", "[← Catalog](README.md)", "", f"{len(templates)} templates.", "", self.TEMPLATE_HEADER]
        L += [self.template_row(t, "catalog") for t in templates]
        return "\n".join(L)

    def render_grouped(self, title: str, intro: str, groups: dict[str, list], link_fmt=None) -> str:
        L = [f"# {title}", "", "[← Catalog](README.md)", "", intro, ""]
        keys = sorted(groups, key=lambda k: (-len(groups[k]), k.lower(), k))
        L += ["| | Templates |", "|---|---|"]
        L += [f"| [{cell(k)}](#{slugify(k)}) | {len(groups[k])} |" for k in keys]
        L += [""]
        for k in keys:
            heading = link_fmt(k) if link_fmt else cell(k)
            L += [f'<a id="{slugify(k)}"></a>', "", f"## {heading}", ""]
            for t in sorted(groups[k], key=lambda t: ((t.get("title") or t["name"]).lower(), t["name"])):
                L.append(f"- [{cell(t.get('title') or t['name'])}]({self.link(t, 'catalog')}) — {cell(t['_category']['title'])}")
            L += [""]
        return "\n".join(L)

    def render_model_files(self) -> str:
        files: dict[tuple, dict] = {}
        for t in self.templates:
            for m in (t["_wf"] or {}).get("models") or []:
                key = (m["name"], m["directory"])
                entry = files.setdefault(key, {"urls": set(), "templates": []})
                if m["url"]:
                    entry["urls"].add(m["url"])
                entry["templates"].append(t)
        L = ["# Model files", "", "[← Catalog](README.md)", ""]
        L += [
            f"{len(files)} distinct model files referenced by template workflows (from node `properties.models`). "
            "Place each file in `ComfyUI/models/<folder>/`.",
            "",
            "| File | Folder | Download | Used by |",
            "|---|---|---|---|",
        ]
        for (name, directory), e in sorted(files.items(), key=lambda kv: (kv[0][1], kv[0][0].lower())):
            dls = " ".join(f"[link]({u})" for u in sorted(e["urls"]))
            uniq = {t["name"]: t for t in e["templates"]}.values()
            used = ", ".join(f"[{cell(t.get('title') or t['name'])}]({self.link(t, 'catalog')})" for t in sorted(uniq, key=lambda t: t["name"]))
            L.append(f"| `{cell(name)}` | `{cell(directory)}` | {dls} | {used} |")
        return "\n".join(L)

    def render_readme(self) -> str:
        n_api = sum(1 for t in self.templates if not t.get("openSource", True))
        L = [
            "# ComfyUI Workflow Templates — Browsable Catalog",
            "",
            f"A Markdown mirror of every template in [{self.repo}](https://github.com/{self.repo}/tree/{self.ref}/templates), "
            "regenerated automatically by a scheduled GitHub Action. GitHub's web UI truncates that folder "
            "(it holds well over 1,000 files), so this repo gives each template its own page, grouped by category, "
            "with thumbnails, models, required custom nodes, model download links and the notes embedded in the workflow.",
            "",
            self.source_line(),
            "",
        ]
        if self.site_url:
            L += [
                f"### [🔎 Open the interactive template browser →]({self.site_url})",
                "",
                "Search, filter by model / tag / media type, preview, and download any workflow in one click.",
                "",
            ]
        L += [
            f"**{len(self.templates)} templates** in {len(self.categories)} categories "
            f"({len(self.templates) - n_api} open source, {n_api} API).",
            "",
            f"> **Nothing is truncated here.** Upstream `templates/` holds {self.file_count} files "
            f"(workflow JSONs plus their thumbnails, previews and index files), so GitHub's folder view stops at 1,000 "
            f"and hides the rest. This README lists every one of the {len(self.templates) + len(self.unindexed)} "
            "workflow JSONs in that folder"
            + (f", including {len(self.unindexed)} not listed in `index.json`" if self.unindexed else "")
            + ".",
            "",
        ]
        L += self.category_table("root")
        L += self.index_links("root")
        L += self.full_directory()
        if self.unindexed:
            L += ["## Workflows not listed in `index.json`", ""]
            L += [f"- [`{n}`]({self.blob}/{n}.json)" for n in self.unindexed]
            L += [""]
        L += [
            "## How it works",
            "",
            "- `.github/workflows/sync.yml` runs every 6 hours (and on demand). It does a blobless, sparse clone of the "
            "upstream repo that downloads only `templates/*.json` — no images — so it is fast and avoids API rate limits.",
            "- `scripts/build_catalog.py` (standard library only) reads `templates/index.json` plus every workflow JSON and "
            "rewrites `catalog/` and this README. Output has no timestamps, so a commit is made only when upstream changed.",
            "- Thumbnails and downloads link to `raw.githubusercontent.com` on the upstream repo; nothing is re-hosted.",
            "- The interactive browser in `site/` is a static page (no build step) that reads `catalog/templates.json`; "
            "the same Action deploys it to GitHub Pages after every sync.",
            "",
            "Run locally:",
            "",
            "```sh",
            f"git clone --depth 1 --filter=blob:none --sparse https://github.com/{self.repo}.git upstream",
            "git -C upstream sparse-checkout set --no-cone '/templates/*.json'",
            "python3 scripts/build_catalog.py --upstream upstream --out .",
            "python3 -m http.server 8000   # then open http://localhost:8000/site/",
            "```",
        ]
        return "\n".join(L)

    def full_directory(self) -> list[str]:
        """Every workflow, grouped by category — the README's main body."""
        L = ["## Directory of all workflows", ""]
        for c in self.categories:
            L += [
                f'<a id="dir-{c["slug"]}"></a>',
                "",
                f"### {cell(c['title'])} ({len(c['templates'])})",
                "",
                f"[Gallery with thumbnails](catalog/{c['slug']}/README.md)",
                "",
                "| Template | Models | Output | Type | Date | JSON |",
                "|---|---|---|---|---|---|",
            ]
            for t in c["templates"]:
                json_link = f"[json]({self.raw}/{t['name']}.json)" if t["_has_json"] else ""
                L.append(
                    f"| [{cell(t.get('title') or t['name'])}]({self.link(t, 'root')}) "
                    f"| {cell(', '.join(t.get('models') or []))} | {cell(t['_output'])} "
                    f"| {self.kind(t)} | {cell(t.get('date'))} | {json_link} |"
                )
            L += ["", "[↑ Top](#categories)", ""]
        return L

    def summary_json(self) -> str:
        items = []
        for t in self.templates:
            wf = t["_wf"] or {}
            item = {k: v for k, v in t.items() if not k.startswith("_")}
            item.update(
                category=t["_category"]["title"],
                categoryGroup=t["_category"]["group"],
                categoryType=t["_category"]["type"],
                outputType=t["_output"],
                page=f"catalog/{t['_page']}",
                workflowUrl=f"{self.raw}/{t['name']}.json" if t["_has_json"] else None,
                thumbnails=[f"{self.raw}/{f}" for f in self.thumbs(t)],
                customNodes=sorted(set(t.get("requiresCustomNodes") or []) | set(wf.get("custom_nodes") or []), key=lambda s: (s.lower(), s)),
                modelFiles=wf.get("models") or [],
                nodeTypes=dict(sorted((wf.get("node_types") or {}).items())),
            )
            items.append(item)
        doc = {"source": {"repo": self.repo, "ref": self.ref, "commit": self.sha, "commitDate": self.commit_date}, "templates": items}
        return json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True)

    # ---- orchestration

    def build(self) -> None:
        if self.catalog_dir.exists():
            shutil.rmtree(self.catalog_dir)
        for c in self.categories:
            write(self.catalog_dir / c["slug"] / "README.md", self.render_category(c))
            for t in c["templates"]:
                write(self.catalog_dir / t["_page"], self.render_template(t))

        by_title = sorted(self.templates, key=lambda t: (t.get("title") or t["name"]).lower())
        newest = sorted(self.templates, key=lambda t: (t.get("date") or "", t["name"]), reverse=True)
        write(self.catalog_dir / "README.md", self.render_catalog_index())
        write(self.catalog_dir / "all.md", self.render_flat("All templates (A–Z)", by_title))
        write(self.catalog_dir / "newest.md", self.render_flat("Newest templates", newest))

        def group(key_fn):
            g = collections.defaultdict(list)
            for t in self.templates:
                for k in key_fn(t):
                    g[k].append(t)
            return g

        write(
            self.catalog_dir / "by-model.md",
            self.render_grouped("Templates by model", "Model families as declared in `index.json`.", group(lambda t: t.get("models") or ["(none)"])),
        )
        write(
            self.catalog_dir / "by-tag.md",
            self.render_grouped("Templates by tag", "Tags as declared in `index.json`.", group(lambda t: t.get("tags") or ["(none)"])),
        )
        write(
            self.catalog_dir / "custom-nodes.md",
            self.render_grouped(
                "Templates by custom node pack",
                "Packs from `requiresCustomNodes` in `index.json` plus non-core `cnr_id`s found on nodes. Core-only templates are not listed.",
                group(lambda t: sorted(set(t.get("requiresCustomNodes") or []) | set((t["_wf"] or {}).get("custom_nodes") or []))),
                link_fmt=lambda k: f"[{cell(k)}](https://registry.comfy.org/nodes/{k})",
            ),
        )
        write(self.catalog_dir / "model-files.md", self.render_model_files())
        write(self.catalog_dir / "templates.json", self.summary_json())
        write(self.out / "README.md", self.render_readme())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--upstream", type=Path, required=True, help="path to a clone of Comfy-Org/workflow_templates")
    ap.add_argument("--out", type=Path, default=Path("."), help="repo root to write README.md and catalog/ into")
    ap.add_argument("--repo", default="Comfy-Org/workflow_templates")
    ap.add_argument("--ref", default="main", help="branch used for raw/blob links")
    ap.add_argument("--site-url", default="", help="GitHub Pages URL of the interactive browser (linked from the Markdown)")
    args = ap.parse_args()

    cat = Catalog(args.upstream, args.out, args.repo, args.ref, args.site_url)
    cat.build()
    print(f"Wrote {len(cat.templates)} templates in {len(cat.categories)} categories (upstream {cat.sha[:7] or 'unknown'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
