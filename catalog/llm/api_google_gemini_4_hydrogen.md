# Google: Gemini 4 Hydrogen

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_4_hydrogen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_4_hydrogen-1.webp" width="360" alt="Google: Gemini 4 Hydrogen api_google_gemini_4_hydrogen-1.webp">

> Gemini 4 Hydrogen reads one reference image and writes the text you ask for: art-directed prompts, detailed captions, or structured visual breakdowns, in a single pass. Extended thinking keeps long-form visual analysis coherent, so it fits prompt-library building, dataset annotation, and batch creative ideation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_4_hydrogen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_4_hydrogen.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_4_hydrogen` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Google, Google Gemini |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-11-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.0 |
| Usage | 67 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | blue_poppies_field.png |

## Subgraphs

- **Format Output** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringConcatenate` | 3 |  |
| `GeminiNodeV3` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

This is only a demo for how to use LLM node in ComfyUI and save the result, you can use the `preview text` or `save text` node to see the result.

In ComfyUI you can use LLM node to help you refine the prompt, analyze an image, and so on.

</details>
