# Lineart Map: LineArt Preprocessor

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility-lineart-video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-lineart-video-1.webp" width="360" alt="Lineart Map: LineArt Preprocessor utility-lineart-video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-lineart-video-2.webp" width="360" alt="Lineart Map: LineArt Preprocessor utility-lineart-video-2.webp">

> Convert a Video to Lineart/Canny for Control Processors

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-lineart-video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-lineart-video.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/preprocessors)

## Details

| | |
|---|---|
| Name | `utility-lineart-video` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | None |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Download size | 5.0 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 12 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #2 | video | utility-lineart-video-input.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LineArtPreprocessor` | 1 | comfyui_controlnet_aux |
| `MarkdownNote` | 1 |  |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `VHS_VideoCombine` | 1 | comfyui-videohelpersuite |
| `VHS_VideoInfo` | 1 | comfyui-videohelpersuite |

## Notes embedded in the workflow

<details><summary>For Local Users</summary>

## Custom Nodes

- [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
- [Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
