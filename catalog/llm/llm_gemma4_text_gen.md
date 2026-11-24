# Gemma4: Text Generation

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=llm_gemma4_text_gen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_gemma4_text_gen-1.webp" width="360" alt="Gemma4: Text Generation llm_gemma4_text_gen-1.webp">

> Input your text prompt and optionally an image, audio, or video. Generate text output with configurable reasoning, coding, and multilingual support.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_gemma4_text_gen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/llm_gemma4_text_gen.json)
- [Tutorial](https://docs.comfy.org/tutorials/llm/gemma4/gemma4)

## Details

| | |
|---|---|
| Name | `llm_gemma4_text_gen` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Gemma 4 |
| Tags | Text Generation |
| Type | open source |
| Date | 2026-05-01 |
| Author | ComfyUI |
| Download size | 8.4 GB |
| Min ComfyUI version | 0.21.0 |
| Usage | 49 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | the_lily_veil.png |
| input | `LoadAudio` #5 | audio | long_demo.mp3 |
| input | `LoadVideo` #6 | video | video_wan_vace_inpainting_input_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `gemma4_e4b_it_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `TextGenerate` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Related PR: [#13376](https://github.com/Comfy-Org/ComfyUI/pull/13376)

## Model Links

- [Hugging Face:Comfy-Org/gemma-4](https://huggingface.co/Comfy-Org/gemma-4)
- [ModelScope:Comfy-Org/gemma-4](https://modelscope.cn/models/Comfy-Org/gemma-4)

**text_encoders**

- [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) (8.44 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 text_encoders/
│       └── gemma4_e4b_it_fp8_scaled.safetensors
```

---
* Other model weights: https://huggingface.co/Comfy-Org/gemma-4/tree/main/text_encoders

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Gemma4 Core Capabilities</summary>

**Core Capabilities**

[Gemma 4](https://huggingface.co/google/gemma-4-E2B-it) models handle a broad range of tasks across text, vision, and audio. Key capabilities include:

+   **Thinking** – Built-in reasoning mode that lets the model think step-by-step before answering.
+   **Long Context** – Context windows of up to 128K tokens (E2B/E4B) and 256K tokens (26B A4B/31B).
+   **Image Understanding** – Object detection, Document/PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), handwriting recognition, and pointing. Images can be processed at variable aspect ratios and resolutions.
+   **Video Understanding** – Analyze video by processing sequences of frames.
+   **Interleaved Multimodal Input** – Freely mix text and images in any order within a single prompt.
+   **Function Calling** – Native support for structured tool use, enabling agentic workflows.
+   **Coding** – Code generation, completion, and correction.
+   **Multilingual** – Out-of-the-box support for 35+ languages, pre-trained on 140+ languages.
+   **Audio** (E2B and E4B only) – Automatic speech recognition (ASR) and speech-to-translated-text translation across multiple languages.

</details>
