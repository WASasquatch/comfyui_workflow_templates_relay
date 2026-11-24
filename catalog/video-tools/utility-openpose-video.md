# Pose Map: DWPose OpenPose

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility-openpose-video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-openpose-video-1.webp" width="360" alt="Pose Map: DWPose OpenPose utility-openpose-video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-openpose-video-2.webp" width="360" alt="Pose Map: DWPose OpenPose utility-openpose-video-2.webp">

> Convert a Video to a temporally stable Pose Control Map

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-openpose-video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-openpose-video.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/preprocessors)

## Details

| | |
|---|---|
| Name | `utility-openpose-video` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | DWPose |
| Tags | Pose Map |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Download size | 5.0 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 36 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #2 | video | pose_input.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `DWPreprocessor` | 1 |  |
| `MarkdownNote` | 1 |  |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoCombine` | 1 |  |

## Notes embedded in the workflow

<details><summary>For Local Users</summary>

## Custom Nodes

- [Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
- [Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
