# Relight: Beeble SwitchX

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_beeble_switchx_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_image_edit-1.webp" width="360" alt="Relight: Beeble SwitchX api_beeble_switchx_image_edit-1.webp">

> Upload your character image and a reference style/lighting image. Generate an edited output with the reference lighting and style applied to your original image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_beeble_switchx_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_beeble_switchx_image_edit` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SwitchX |
| Tags | API, Relight, Image Edit |
| Type | API |
| Date | 2026-05-29 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 27 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | soft_light_headphones_man.png |
| input | `LoadImage` #17 | image | simple_modern_living_space.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `SaveImage` | 2 |  |
| `BeebleSwitchXImageEdit` | 1 |  |
| `ImageCompare` | 1 |  |
| `InvertMask` | 1 |  |
| `JoinImageWithAlpha` | 1 |  |
| `MarkdownNote` | 1 |  |

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
