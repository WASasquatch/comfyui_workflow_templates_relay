# Normal Map: NormalCrafter

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-normal_crafter-video-1.webp" width="360" alt="Normal Map: NormalCrafter utility-normal_crafter-video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-normal_crafter-video-2.webp" width="360" alt="Normal Map: NormalCrafter utility-normal_crafter-video-2.webp">

> Convert a Video to a temporally stable Normal Map

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-normal_crafter-video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-normal_crafter-video.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/preprocessors)

## Details

| | |
|---|---|
| Name | `utility-normal_crafter-video` |
| Category | Foundation › Video Tools |
| Media type | image |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.0.1 |
| Usage | 15 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #3 | video | normals_input.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `NormalCrafterNode` | 1 |  |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoCombine` | 1 |  |
| `VHS_VideoInfo` | 1 |  |

## Notes embedded in the workflow

<details><summary>For Local Users</summary>

## Custom Nodes

- [ComfyUI-NormalCrafterWrapper](https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper)
- [Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
