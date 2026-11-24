# LivePortrait for Facial Expression

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_liveportrait.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_liveportrait.app-1.webp" width="360" alt="LivePortrait for Facial Expression templates_liveportrait.app-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_liveportrait.app-2.webp" width="360" alt="LivePortrait for Facial Expression templates_liveportrait.app-2.webp">

> Upload a portrait image and a reference expression video. Generate a video of the portrait with the facial expressions from the reference.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_liveportrait.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_liveportrait.app.json)

## Details

| | |
|---|---|
| Name | `templates_liveportrait.app` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | LivePortrait |
| Tags | Video, Lip Sync |
| Type | open source |
| Date | 2026-03-06 |
| Author | shane |
| Download size | 20.0 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 26 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | live_portrait_character.png |
| input | `VHS_LoadVideo` #44 | video | live_portrait_expression.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-liveportraitkj](https://registry.comfy.org/nodes/comfyui-liveportraitkj)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageResizeKJv2` | 2 | comfyui-kjnodes |
| `DownloadAndLoadLivePortraitModels` | 1 | comfyui-liveportraitkj |
| `LivePortraitComposite` | 1 | comfyui-liveportraitkj |
| `LivePortraitCropper` | 1 | comfyui-liveportraitkj |
| `LivePortraitLoadMediaPipeCropper` | 1 | comfyui-liveportraitkj |
| `LivePortraitProcess` | 1 | comfyui-liveportraitkj |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `VHS_VideoCombine` | 1 | comfyui-videohelpersuite |
