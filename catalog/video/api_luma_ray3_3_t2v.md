# Luma Ray 3.2: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_luma_ray3_3_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_ray3_3_t2v-1.webp" width="360" alt="Luma Ray 3.2: Text to Video api_luma_ray3_3_t2v-1.webp">

> Generate cinematic-quality videos from text prompts using Luma Ray 3.2, with optional video extension by providing a generation ID from a previous run. Ideal for creating short film sequences, marketing content, and iterative video refinement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_ray3_3_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_luma_ray3_3_t2v.json)

## Details

| | |
|---|---|
| Name | `api_luma_ray3_3_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Luma |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-06-18 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.0 |
| Usage | 5 |
| Nodes | 6 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 2 |  |
| `LumaRay32ExtendVideoNode` | 1 |  |
| `LumaRay32TextToVideoNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Extend Video</summary>

This section extends videos and needs a `generation_id` from the upstream Luma Ray 3.2 node.

1. By default, `source_generation_id` is wired automatically. To extend from a previous run instead, disconnect that input and paste the `generation_id` shown in **Preview as Text (generation_id)**.
2. Select this section and press **Ctrl+B** to enable it when you want to extend the video.

</details>
