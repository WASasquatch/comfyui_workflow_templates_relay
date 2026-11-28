# Kling O3: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_o3_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_i2v-1.webp" width="360" alt="Kling O3: Reference to Video api_kling_o3_i2v-1.webp">

> Upload a reference image and optional audio or text prompt. Generate a character-consistent video with native audio output and precise storyboard control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_i2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_o3_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling O3 |
| Tags | API, Character Reference, Image to Video |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 36 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | chasing_the_light.png |
| output | `SaveVideo` #20 | video | kling_o3_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProImageToVideoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Select the Batch Images node, then press Ctrl+B to enable multiple image input.
```

</details>
