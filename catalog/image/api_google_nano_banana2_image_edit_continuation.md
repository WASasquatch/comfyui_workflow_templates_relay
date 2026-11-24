# Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit_continuation-1.webp" width="360" alt="Image Edit api_google_nano_banana2_image_edit_continuation-1.webp">

> Start with an image and an empty prompt, then describe the edit you want. Nano Banana 2 generates a modified image while preserving subject consistency and high visual fidelity.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit_continuation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_nano_banana2_image_edit_continuation.json)

## Details

| | |
|---|---|
| Name | `api_google_nano_banana2_image_edit_continuation` |
| Category | Foundation › Image |
| Media type | image |
| Models | Google, Nano Banana 2 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 17 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | saintly_rose_portrait.png |
| output | `SaveImage` #4 | image | api_google_nano_banana2_image_edit_continuation.png |

## Subgraphs

- **Edit Image (Nano Banana 2)** (1 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>What to do</summary>

## Describe your edit

Write what you want to change in the prompt above, then click **Run**.

</details>
