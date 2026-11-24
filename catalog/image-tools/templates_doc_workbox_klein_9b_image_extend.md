# Image Outpainting: FLUX.2 Klein 9B

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_doc_workbox_klein_9b_image_extend-1.webp" width="360" alt="Image Outpainting: FLUX.2 Klein 9B templates_doc_workbox_klein_9b_image_extend-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_doc_workbox_klein_9b_image_extend-2.webp" width="360" alt="Image Outpainting: FLUX.2 Klein 9B templates_doc_workbox_klein_9b_image_extend-2.webp">

> Use the FLUX.2 Klein 9B model to intelligently extend and expand image content. Input an image to generate seamless outpainting and extended compositions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_doc_workbox_klein_9b_image_extend.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_doc_workbox_klein_9b_image_extend.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-klein)

## Details

| | |
|---|---|
| Name | `templates_doc_workbox_klein_9b_image_extend` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | FLUX.2 Klein |
| Tags | Image, Outpainting |
| Type | open source |
| Date | 2026-03-19 |
| Author | Doc_workBox |
| Download size | 15.6 GB |
| Min ComfyUI version | 0.9.2 |
| Usage | 265 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #159 | image | red_panda.png |
| output | `SaveImage` #142 | image | templates_doc_workbox_klein_9b_image_extend.png |

## Custom nodes required

- [ComfyUI-Color-Matcher](https://registry.comfy.org/nodes/ComfyUI-Color-Matcher)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI_Swwan](https://registry.comfy.org/nodes/ComfyUI_Swwan)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-9b.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/resolve/main/flux-2-klein-9b.safetensors) |
| `qwen_3_8b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/vae-text-encorder-for-flux-klein-9b/resolve/main/split_files/text_encoders/qwen_3_8b.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageScaleToTotalPixels` | 2 | comfy-core |
| `ReferenceLatent` | 2 |  |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ColorMatch` | 1 |  |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DrawMaskOnImage` | 1 |  |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `Flux2Scheduler` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `ImagePadForOutpaint` | 1 |  |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 |  |
| `VAELoader` | 1 | comfy-core |
