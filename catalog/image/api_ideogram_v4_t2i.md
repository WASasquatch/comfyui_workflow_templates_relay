# Ideogram v4: Text to Image (API)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_t2i-1.webp" width="360" alt="Ideogram v4: Text to Image (API) api_ideogram_v4_t2i-1.webp">

> Input a text prompt in structured JSON format. Generate a high-quality image with precise layout control, text rendering, and color palette support.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_t2i.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Ideogram |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-06-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.2 |
| Usage | 18 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #6 | image | api_ideogram_v4_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNodeV3` | 1 |  |
| `IdeogramV4` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Ideogram 4 (API)</summary>

## What this workflow does

**Generate path (connected):**

`IdeogramV4` → `Save Image`

1. **IdeogramV4**: partner API node. You can type **plain natural language** in the prompt field, but this workflow uses **structured JSON** for stronger control (layout, colors, in-image text, per-object `bbox`). There is no separate negative prompt field.
2. **Save Image**: writes output with filename prefix `ideogram_v4`.

**JSON Prompt Builder (Gemini):**

Use **Gemini** (`Gemini 3.7 Flash`) to help build the **IdeogramV4** prompt: describe your idea in the user prompt field; the model returns schema-matching JSON. Connect **STRING** → **IdeogramV4** `prompt` if you want it wired in, or paste / type the result manually. This workflow leaves that link open so the bundled JSON example stays in **IdeogramV4** by default.

---

## Prompt format

- **Natural language** — allowed; quickest for simple ideas.
- **JSON** (as in this file) — better control over style palette, element placement (`bbox`), and literal text in the image; recommended for posters like the default example.

</details>
