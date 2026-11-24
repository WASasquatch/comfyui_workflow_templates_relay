# Audio Separation

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-audioseparation-1.webp" width="360" alt="Audio Separation utility-audioseparation-1.webp">

> Input Music → Separate Vocals / Bass / Drums / Other

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-audioseparation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-audioseparation.json)

## Details

| | |
|---|---|
| Name | `utility-audioseparation` |
| Category | Foundation › Audio |
| Media type | image |
| Tags | Audio, Audio Editing |
| Type | open source |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 48 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #9 | audio | utility-audioseparation-audio-input.mp3 |

## Custom nodes required

- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveAudioAdvanced` | 4 | comfy-core |
| `AudioStemSeparate` | 1 |  |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |

## Notes embedded in the workflow

<details><summary>For Local Users</summary>

## Custom Nodes

- [lum3on/ComfyUI_AudioTools](https://github.com/lum3on/ComfyUI_AudioTools)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
