# Remove Background: BiRefNet

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_birefnet_remove_background)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_birefnet_remove_background-1.webp" width="360" alt="Remove Background: BiRefNet utility_birefnet_remove_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_birefnet_remove_background-2.webp" width="360" alt="Remove Background: BiRefNet utility_birefnet_remove_background-2.webp">

> Upload an image with any background. Generate a version with the background removed and a precision segmentation mask.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_birefnet_remove_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_birefnet_remove_background.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/remove-background-birefnet)

## Details

| | |
|---|---|
| Name | `utility_birefnet_remove_background` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | BiRefNet |
| Tags | Remove Background |
| Type | open source |
| Date | 2026-05-10 |
| Author | ComfyUI |
| Download size | 409.6 MB |
| Min ComfyUI version | 0.21.0 |
| Usage | 85 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | the_lily_veil.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |

## Subgraphs

- **Remove Background (BiRefNet)** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `InvertMask` | 1 |  |
| `JoinImageWithAlpha` | 1 |  |
| `LoadBackgroundRemovalModel` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `MaskPreview` | 1 |  |
| `PreviewImage` | 1 |  |
| `RemoveBackground` | 1 |  |

## Notes embedded in the workflow

<details><summary>Model Link</summary>

## Model Links

- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet)

### Alternative Repos

- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) (423.9 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 background_removal/
│       └── birefnet.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
