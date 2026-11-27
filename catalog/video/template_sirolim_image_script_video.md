# Image to Script to Kling Video Generation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_sirolim_image_script_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_image_script_video-1.webp" width="360" alt="Image to Script to Kling Video Generation template_sirolim_image_script_video-1.webp">

> Upload an image to automatically generate a descriptive script. This script is then used to create a video with the Kling 3.0 Omni model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_image_script_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_sirolim_image_script_video.json)

## Details

| | |
|---|---|
| Name | `template_sirolim_image_script_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Google Gemini, Kling O3, Nano Banana 2 |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2026-03-09 |
| Author | sirolim |
| Min ComfyUI version | 0.46.4 |
| Usage | 18 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | input_storyboard_video.jpg |
| output | `SaveVideo` #7 | video | output_image_script_video.mp4 |

## Subgraphs

- **Prompt A** (1 nodes)
- **Prompt B** (1 nodes)
- **Prompt C** (1 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 4 |  |
| `OpenAIChatNodeV2` | 3 |  |
| `GeminiImage2Node` | 1 |  |
| `GeminiNodeV3` | 1 |  |
| `KlingOmniProImageToVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewImage` | 1 |  |
| `PrimitiveNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Image -> Script -> Video</summary>

Upload an **image** write a script, generate a video.

## How It Works

1. **Upload an image**
2. Set your output **aspect ratio**
3. Write a brief prompt with details that are important for you.

4. The system:
   - Creates a script with 3 prompts
   - Creates a start image

   and generates:
   - a video

That’s it.  
Image -> Script -> Video

</details>
