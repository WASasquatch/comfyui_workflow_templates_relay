# Face Detection: MediaPipe

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_face_detection_mediapipe-1.webp" width="360" alt="Face Detection: MediaPipe utility_face_detection_mediapipe-1.webp">

> Input an image and detect up to 6 facial landmarks per face, enabling ultrafast multi-face detection

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_face_detection_mediapipe.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_face_detection_mediapipe.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/face-detection/mediapipe)

## Details

| | |
|---|---|
| Name | `utility_face_detection_mediapipe` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Mediapipe |
| Tags | Element Segmentation |
| Type | open source |
| Date | 2026-05-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Distributions | cloud |
| Usage | 34 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | soft_neon_girl.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `mediapipe_face_fp32.safetensors` | `detection` | [link](https://huggingface.co/Comfy-Org/mediapipe/resolve/main/detection/mediapipe_face_fp32.safetensors) |

## Subgraphs

- **Face Detection (Mediapipe)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `PreviewImage` | 2 | comfy-core |
| `DrawBBoxes` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMediaPipeFaceLandmarker` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `MediaPipeFaceLandmarker` | 1 | comfy-core |
| `MediaPipeFaceMask` | 1 | comfy-core |
| `MediaPipeFaceMeshVisualize` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Setup & links</summary>

## Setup & links

## Model Links

- [Hugging Face:Comfy-Org/mediapipe](https://huggingface.co/Comfy-Org/mediapipe)

### Alternative Repos

- [ModelScope:Comfy-Org/mediapipe](https://modelscope.cn/models/Comfy-Org/mediapipe)

- MediaPipe (upstream): [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)
- ComfyUI feature: [#14009 — MediaPipe face detection](https://github.com/Comfy-Org/ComfyUI/pull/14009)
- Subgraphs guide: [docs.comfy.org — Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model (local)

**detection**

- [mediapipe_face_fp32.safetensors](https://huggingface.co/Comfy-Org/mediapipe/resolve/main/detection/mediapipe_face_fp32.safetensors) (5.2 MB)

## Model path

```
ComfyUI/
└── models/
    └── detection/
        └── mediapipe_face_fp32.safetensors
```

## Report issues

Update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and download the model above. Desktop/Cloud may lag nightly builds.

- Runtime / backend: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow templates: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MediaPipe Face Detection</summary>

## MediaPipe Face Detection

**Scope (PR [#14009](https://github.com/Comfy-Org/ComfyUI/pull/14009))**  
Face only — BlazeFace + FaceMesh v2 + ARKit blendshapes. Not hand/pose/holistic. Upstream: [MediaPipe](https://github.com/google-ai-edge/mediapipe).

**This workflow**  
One subgraph drives detection; **Mask** and **Visualize** groups preview mask vs mesh/bboxes.

---

### Subgraph inputs

| Pin | Description |
|-----|-------------|
| **image** | Input image batch to analyze. |
| **face_landmarker** | Optional. Leave empty to use the built-in loader + `model_name` below. Connect an external `FACE_DETECTION_MODEL` to override. |

### Subgraph parameters

| Parameter | Description |
|-----------|-------------|
| **model_name** | Checkpoint in `ComfyUI/models/detection/` (default: `mediapipe_face_fp32.safetensors`). If this shows an error, download the model (see **Setup & links** note). |
| **detector_variant** | **short** — close / large faces (~2 m). **full** — smaller or farther faces (~5 m), slower. **both** — runs both per frame and keeps the variant that found more faces (~2× cost). |
| **num_faces** | Max faces per frame. **0** = no limit (return all detections). **1–16** = cap count (highest scores kept). |
| **custom_face_oval** | Include face-outline region in the **mask** output. |
| **custom_lips** | Include lips in the mask (union with other enabled regions). |
| **custom_left_eye** | Include left eye region in the mask. |
| **custom_right_eye** | Include right eye region in the mask. |
| **custom_irises** | Include iris regions in the mask. |

Mask toggles use **custom** mode internally: only checked regions are filled; multiple ON regions are **unioned** into one mask per frame.

### Subgraph outputs

| Pin | Description |
|-----|-------------|
| **face_landmarks** | Per-frame faces: 478 landmarks, blendshapes, mesh topology (for mesh viz nodes). |
| **bboxes** | Face bounding boxes — fed to **Draw BBoxes** in the Visualize group. |
| **mask** | Binary mask from the region toggles above. |

### Inside the subgraph (not on the widget panel)

Open the subgraph for advanced detection options: **min_confidence** (detection threshold), **missing_frame_fallback** (`empty` / `previous` / `interpolate` for failed frames in video batches).

**Visualize group** uses separate nodes: mesh connection preset, color, line thickness (not exposed on the subgraph shell).

</details>
