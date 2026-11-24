# Character & Outfit to Fashion Video

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-stitched_vid_contact_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-stitched_vid_contact_sheet-1.webp" width="360" alt="Character & Outfit to Fashion Video templates-stitched_vid_contact_sheet-1.webp">

> Upload your character and clothing items or accessories. Generate a fashion photograph base and use as a reference to 8x grid images, together with Multi-Keyframe Video Stitching.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-stitched_vid_contact_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-stitched_vid_contact_sheet.json)

## Details

| | |
|---|---|
| Name | `templates-stitched_vid_contact_sheet` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Google Gemini Image, Nano Banana Pro, Google, Kling, Kling O1, OpenAI |
| Tags | Image to Video, FLF2V, API |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 9 |
| Nodes | 241 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | subject_leopard_hair_croc_jacket.png |
| input | `LoadImage` #26 | image | cartier-glasses-1.jpg |
| input | `LoadImage` #27 | image | outfit_image-2.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Batch Images** (5 nodes)
- **Batch Images** (4 nodes)
- **Batch Images** (5 nodes)
- **Crop Images** (21 nodes)
- **Crop Images** (21 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Merge Videos** (12 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Generate Video (Kling)** (8 nodes)
- **Merge Videos** (12 nodes)
- **Merge Videos** (12 nodes)
- **Merge Videos** (12 nodes)
- **Merge Videos** (12 nodes)
- **Merge Videos** (12 nodes)
- **Merge Videos** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 16 | comfy-core |
| `ImageFromBatch` | 16 | comfy-core |
| `SimpleMath+` | 16 | comfyui_essentials |
| `ComfySwitchNode` | 14 | comfy-core |
| `GetVideoComponents` | 14 | comfy-core |
| `PrimitiveBoolean` | 14 | comfy-core |
| `ResizeAndPadImage` | 13 | comfy-core |
| `GetImageSize` | 12 | comfy-core |
| `PreviewImage` | 12 | comfy-core |
| `SaveImage` | 11 | comfy-core |
| `PrimitiveInt` | 10 | comfy-core |
| `SaveVideo` | 9 | comfy-core |
| `ComfyMathExpression` | 8 | comfy-core |
| `GeminiNode` | 8 | comfy-core |
| `ImageCrop` | 8 | comfy-core |
| `KlingStartEndFrameNode` | 8 | comfy-core |
| `PreviewAny` | 8 | comfy-core |
| `AudioMerge` | 7 | comfy-core |
| `CreateVideo` | 7 | comfy-core |
| `EmptyAudio` | 7 | comfy-core |
| `ImageBatch` | 5 | comfy-core |
| `PrimitiveStringMultiline` | 4 | comfy-core |
| `GeminiImage2Node` | 3 | comfy-core |
| `LoadImage` | 3 | comfy-core |
| `ImageBatchMulti` | 2 | comfyui-kjnodes |
| `ImageResizeKJv2` | 2 | comfyui-kjnodes |
| `Reroute` | 2 |  |
| `GetImagesFromBatchIndexed` | 1 | comfyui-kjnodes |
| `RegexReplace` | 1 | comfy-core |
