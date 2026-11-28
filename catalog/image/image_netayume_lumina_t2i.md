# NetaYume Lumina Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_netayume_lumina_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_netayume_lumina_t2i-1.webp" width="360" alt="NetaYume Lumina Text to Image image_netayume_lumina_t2i-1.webp">

> High-quality anime-style image generation with enhanced character understanding and detailed textures. Fine-tuned from Neta Lumina on Danbooru dataset.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_netayume_lumina_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_netayume_lumina_t2i.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/newbie-image/newbie-image-exp-0-1)

## Details

| | |
|---|---|
| Name | `image_netayume_lumina_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | OmniGen |
| Tags | Anime, Image, Text to Image |
| Type | open source |
| Date | 2025-10-10 |
| Author | ComfyUI |
| Download size | 9.9 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 33 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_netayume_lumina_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `NetaYumev35_pretrained_all_in_one.safetensors` | `checkpoints` | [link](https://huggingface.co/duongve/NetaYume-Lumina-Image-2.0/resolve/main/NetaYumev35_pretrained_all_in_one.safetensors) |

## Subgraphs

- **Text to Image (NetaYume Lumina)** (11 nodes)
- **CLIP Text Encode (Negative Prompt)** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `PrimitiveStringMultiline` | 4 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `StringConcatenate` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Image size</summary>

This model is best at 1024x1024, but you can try higher like 1024x1536

</details>

<details><summary>Note: Prompt</summary>

You should keep the prefix part fixed until the **Prompt Start** tag

@whatever in the prompt is for artist tags, such as @comfyanonymous

</details>

<details><summary>Note: About NetaYume Lumina</summary>

## About NetaYume Lumina

[NetaYume Lumina](https://civitai.com/models/1790792) is a **text-to-image** model fine-tuned from [Neta Lumina](https://huggingface.co/neta-art/Neta-Lumina), a high-quality anime-style image generation model developed by [**Neta.art Lab**](https://huggingface.co/neta-art). It builds upon [**Lumina-Image-2.0**,](https://huggingface.co/Alpha-VLLM/Lumina-Image-2.0) an open-source base model released by the [**Alpha-VLLM team**](https://huggingface.co/Alpha-VLLM) at Shanghai AI Laboratory.

**Key Features:**

- **High-Quality Anime Generation:** Generates detailed anime-style images with sharp outlines, vibrant colors, and smooth shading.
- **Improved Character Understanding:** Better captures characters, especially those from the Danbooru dataset, resulting in more coherent and accurate character representations.
- **Enhanced Fine Details:** Accurately generates accessories, clothing textures, hairstyles, and background elements with greater clarity.


## Model link


Download this file: [NetaYumev35_pretrained_all_in_one.safetensors](https://huggingface.co/duongve/NetaYume-Lumina-Image-2.0/resolve/main/NetaYumev35_pretrained_all_in_one.safetensors) (9.89 GB) 

Then place it in the **ComfyUI/models/checkpoints** folder.

</details>

<details><summary>Note: Prompt</summary>

Check the prompt book [here](https://nieta-art.feishu.cn/wiki/RY3GwpT59icIQlkWXEfcCqIMnQd)

You should keep the prefix part fixed until the **Prompt Start** tag

@whatever in the prompt is for artist tags, such as @comfyanonymous

</details>
