# Frame Interpolation: FILM or RIFE

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_video_frame_interpolation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_frame_interpolation-1.webp" width="360" alt="Frame Interpolation: FILM or RIFE utility_video_frame_interpolation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_frame_interpolation-2.webp" width="360" alt="Frame Interpolation: FILM or RIFE utility_video_frame_interpolation-2.webp">

> Upload a video and select either RIFE or FILM frame interpolation model to generate smoother, higher frame rate video output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_frame_interpolation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_video_frame_interpolation.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/frame-interpolation)

## Details

| | |
|---|---|
| Name | `utility_video_frame_interpolation` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | FILM, RIFE |
| Tags | Frame Interpolation |
| Type | open source |
| Date | 2026-04-27 |
| Author | ComfyUI |
| Download size | 102.4 MB |
| Min ComfyUI version | 0.20.0 |
| Usage | 55 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #4 | video | white_armored_warrior.mp4 |
| output | `SaveVideo` #7 | video | utility_video_frame_interpolation.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `film_net_fp16.safetensors` | `frame_interpolation` | [link](https://huggingface.co/Comfy-Org/frame_interpolation/resolve/main/frame_interpolation/film_net_fp16.safetensors) |

## Subgraphs

- **Frame Interpolation** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `FrameInterpolate` | 1 | comfy-core |
| `FrameInterpolationModelLoader` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Link</summary>

**Input Assets**
- [white_armored_warrior.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/white_armored_warrior.mp4) — required workflow input (`input/white_armored_warrior.mp4`)

Related PR: [#13258](https://github.com/Comfy-Org/ComfyUI/pull/13258)

## Model Links

- [Hugging Face:Comfy-Org/frame_interpolation](https://huggingface.co/Comfy-Org/frame_interpolation)

### Alternative Repos

- [ModelScope:Comfy-Org/frame_interpolation](https://modelscope.cn/models/Comfy-Org/frame_interpolation)

**frame_interpolation**

- [film_net_fp16.safetensors](https://huggingface.co/Comfy-Org/frame_interpolation/resolve/main/frame_interpolation/film_net_fp16.safetensors) (65.7 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 frame_interpolation/
│   │   ├── film_net_fp16.safetensors (current template)
│   │   ├── rife_v4.25.safetensors
│   │   ├── rife_v4.25_heavy.safetensors
│   │   ├── rife_v4.25_lite.safetensors
│   │   ├── rife_v4.26.safetensors
│   │   └── rife_v4.26_heavy.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
