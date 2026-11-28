# Video Edit: Beeble SwitchX

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_beeble_switchx_video_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_video_edit-1.webp" width="360" alt="Video Edit: Beeble SwitchX api_beeble_switchx_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_video_edit-2.webp" width="360" alt="Video Edit: Beeble SwitchX api_beeble_switchx_video_edit-2.webp">

> Upload a source video and a reference image, then provide a prompt describing the desired environment and lighting. Generate an edited video where masked regions follow your prompt and reference, while unmasked regions preserve the original pixels and motion, plus an alpha matte for compositing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_beeble_switchx_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_beeble_switchx_video_edit` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | SwitchX |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-05-29 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 149 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | blue_poppies_field.png |
| input | `LoadVideo` #21 | video | woman_in_wheat_field.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 2 |  |
| `BeebleSwitchXVideoEdit` | 1 |  |
| `GetImageSize` | 1 |  |
| `GetVideoComponents` | 1 |  |
| `LoadImage` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>Beeble SwitchX Image Edit</summary>

## Beeble SwitchX — Image Edit

**Switch anything, keep what matters.** Masked regions follow your prompt and reference; unmasked regions keep the source pixels and are relit to match.

---

### What this graph does

1. **Source image** — the still SwitchX edits.
2. **Reference image** (optional) — visual blueprint for background, lighting, mood, and costumes. Masked areas are filled from it; the subject adopts its look without replacing unmasked pixels.
3. **Beeble API** — uploads both, runs SwitchX, then downloads the **render** and the **alpha matte** Beeble used.
4. **Outputs you get:** the composited result, a before/after compare, and (via alpha) a transparent cutout PNG.

At least one of **prompt** or **reference_image** is required.

---

### Alpha modes

| Comfy | Beeble | Best for |
|-------|--------|----------|
| **auto** | Auto | Background swap, relighting, virtual production |
| **select** | Select | Targeted edits (outfit, inpainting); connect your mask |
| **fill** | Fill | Full-frame relight/restyle; no separate alpha output |
| **custom** | Upload | Custom matte from Nuke, After Effects, etc. |

---

### Prompting 

Be specific — environment, lighting, mood:

*"A dramatic cliff in Ireland, soft overcast lighting, highly detailed props."*

Avoid vague prompts (e.g. *"Take me to heaven"*).

**Reference image:** does not need to match the source perfectly; SwitchX keeps your real pixels outside the mask and only pulls style/lighting from the reference.

Video: use **Beeble SwitchX Video Edit** (max 240 frames).

</details>
