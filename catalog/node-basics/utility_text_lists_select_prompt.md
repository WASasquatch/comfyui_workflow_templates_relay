# Batch Process Text Prompts From List

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_text_lists_select_prompt)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_text_lists_select_prompt-1.webp" width="360" alt="Batch Process Text Prompts From List utility_text_lists_select_prompt-1.webp">

> Loads and executes a workflow sequentially using prompts from a text list. Iterates through each entry to generate multiple outputs from a single batch operation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_text_lists_select_prompt.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_text_lists_select_prompt.json)

## Details

| | |
|---|---|
| Name | `utility_text_lists_select_prompt` |
| Category | Foundation › Node Basics |
| Output | image |
| Models | Z-Image-Turbo |
| Tags | Batch Generation |
| Type | open source |
| Date | 2026-03-30 |
| Author | ComfyUI |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 17 |
| Nodes | 13 |

## Custom nodes required

- [FL_PromptSelectorBasic](https://registry.comfy.org/nodes/FL_PromptSelectorBasic)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Z-Image-Turbo)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `FL_PromptSelectorBasic` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveInt` | 1 |  |
| `SaveImage` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# 🔢 FL Prompt Selector

Walks through a list of prompts one at a time using an **Int node as the index**.  
Connect it to a Blueprint or Partner Node to run one prompt per batch step.

---

## How it works

Write one prompt per line in the prompts field — the Int node selects which line 
to use by index. In a batched run, the index increments automatically with each step.

If your batch has more runs than lines in your list, it **loops back to the top**.

---

## What's an Int?

An **Int** (integer) is a whole number node — it holds a single number value like 
`0`, `1`, or `2`. Here it acts as a pointer, telling the selector which line in 
your prompt list to use. Index `0` = first line, `1` = second line, and so on.

---

## Setup

1. Write each prompt on its own line
2. Connect an **Int node** to the `index` input to control the starting position
3. Connect the **STRING output** to a Blueprint or Partner Node
4. Set your batch size — the node will walk the list automatically

---

_💡 Set the Int node to 0 to always start from the top of your list._

</details>
