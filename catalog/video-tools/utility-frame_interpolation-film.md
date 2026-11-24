# Frame Interpolation: FILM

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility-frame_interpolation-film)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-frame_interpolation-film-1.webp" width="360" alt="Frame Interpolation: FILM utility-frame_interpolation-film-1.webp">

> Smooth out low frame-rate videos

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-frame_interpolation-film.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-frame_interpolation-film.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/frame-interpolation)

## Details

| | |
|---|---|
| Name | `utility-frame_interpolation-film` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | None |
| Tags | Frame Interpolation |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Download size | 5.0 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 11 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #3 | video | frame_interpolation-input.mp4 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FILM VFI` | 1 |  |
| `MarkdownNote` | 1 |  |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoCombine` | 1 |  |
| `VHS_VideoInfo` | 1 |  |

## Notes embedded in the workflow

<details><summary>For Local Users</summary>

## Required Custom Nodes

- [annovel16/ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation)
- [Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)


## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
