# Depth Map: Depth Anything v2

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-depthAnything-v2-relative-video-1.webp" width="360" alt="Depth Map: Depth Anything v2 utility-depthAnything-v2-relative-video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-depthAnything-v2-relative-video-2.webp" width="360" alt="Depth Map: Depth Anything v2 utility-depthAnything-v2-relative-video-2.webp">

> Convert a Video to a temporally stable Depth Map

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-depthAnything-v2-relative-video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-depthAnything-v2-relative-video.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/preprocessors)

## Details

| | |
|---|---|
| Name | `utility-depthAnything-v2-relative-video` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | Depth Anything v2 |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Download size | 1.0 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 26 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #6 | video | roller_coaster.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `DepthAnything_V2` | 1 |  |
| `DownloadAndLoadDepthAnythingV2Model` | 1 |  |
| `MarkdownNote` | 1 |  |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoCombine` | 1 |  |
| `VHS_VideoInfo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

**depthanything**

- [depth_anything_v2_vitl_fp32.safetensors](https://huggingface.co/Kijai/DepthAnythingV2-safetensors/resolve/main/depth_anything_v2_vitl_fp32.safetensors) (1.25 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 depthanything/
│   │   ├── depth_anything_v2_vitl_fp32.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
