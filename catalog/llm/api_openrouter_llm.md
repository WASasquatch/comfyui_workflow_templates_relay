# OpenRouter LLM

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_llm-1.webp" width="360" alt="OpenRouter LLM api_openrouter_llm-1.webp">

> Select a model from OpenRouter’s curated list (Claude, GPT, Gemini, etc.). Generate a text response with optional media uploads for vision-capable models.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_llm.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_llm.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_llm` |
| Category | Foundation › LLM |
| Media type | image |
| Models | OpenRouter |
| Tags | Text Generation, API |
| Type | API |
| Date | 2026-05-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.22.1 |
| Usage | 15 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | contact_sheet_app_input_1.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `OpenRouterLLMNode` | 1 |  |
| `PreviewAny` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# OpenRouter LLM

This API node sends chat requests through OpenRouter using a curated model list (Claude, GPT, Gemini, Grok, DeepSeek, Qwen, Mistral, GLM, Kimi, Perplexity Sonar, and others).

## Inputs change with the selected model

The **model** dropdown is a dynamic combo: switching models updates which inputs appear and how many media slots you get.

- **Images / videos** — Shown only for vision-capable models. Max slots vary by model (e.g. up to 20 images on Claude, GPT, Grok, and Gemini; 10 on Qwen and Kimi; 8 on Mistral). Gemini 3.5 Flash and Qwen 3.6 Plus/Flash also expose video inputs.
- **Reasoning effort** — Available on reasoning and frontier-reasoning models (`off` / `low` / `medium` / `high`). Not shown on standard text-only models.
- **Search context size** — Available on Perplexity Sonar models for web-grounded answers.

Models without vision support hide image and video inputs entirely.

## This workflow

1. **Load Image** feeds a reference into the model’s image slot(s).
2. **OpenRouter LLM** analyzes the image and returns a text-to-image prompt (see **prompt** and **system_prompt** on the node).
3. **Preview Any** displays the string for copy-paste into downstream image generation nodes.

Token pricing is shown on the node badge and depends on the selected model.

</details>
