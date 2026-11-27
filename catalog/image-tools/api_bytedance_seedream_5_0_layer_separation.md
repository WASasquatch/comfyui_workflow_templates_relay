# Layer Decomposition: Seedream 5.0 Pro

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_seedream_5_0_layer_separation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_layer_separation-1.webp" width="360" alt="Layer Decomposition: Seedream 5.0 Pro api_bytedance_seedream_5_0_layer_separation-1.webp">

> Split any image into independent, editable layers — subject, product, background, and text — with a single text instruction using Seedream 5.0 Pro. A single poster can yield 10+ layers, with design-grade text separation supporting multilingual headlines and CJK fonts. Ideal for brand design, e-commerce asset creation, and layout iteration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_layer_separation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_0_layer_separation.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream_5_0_layer_separation` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Seedream 5.0 Pro |
| Tags | API, Layer Decompose |
| Type | API |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.3 |
| Usage | 93 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #15 | image | victory_cover.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 |  |
| `BatchMasksNode` | 1 |  |
| `ByteDanceSeedreamLayerSeparationNodeV2` | 1 |  |
| `ImageCompositor` | 1 |  |
| `JoinImageWithAlpha` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Edit layers</summary>

```text
Switch to Nodes2.0 then click the `Open Compositor`
```

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [victory_cover.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/victory_cover.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
