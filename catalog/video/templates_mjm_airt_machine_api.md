# AIrt MAchIne (API version)

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_mjm_airt_machine_api)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_airt_machine_api-1.webp" width="360" alt="AIrt MAchIne (API version) templates_mjm_airt_machine_api-1.webp">

> Upload an image to generate a unique, looping AI video. The workflow uses an LLM to create prompts, employs Kling3.0 for video generation, and stitches the clips into a seamless final loop.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_airt_machine_api.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_mjm_airt_machine_api.json)

## Details

| | |
|---|---|
| Name | `templates_mjm_airt_machine_api` |
| Category | Foundation › Video |
| Output | video |
| Models | Google Gemini, Kling 3.0, Z-Image-Turbo |
| Tags | API, FLF2V, Video |
| Type | API |
| Date | 2026-03-03 |
| Author | Julien \| MJM |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 10 |
| Nodes | 132 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #94 | image | AIrt_MAchIne_init.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `4x-UltraSharp.safetensors` | `upscale_models` | [link](https://huggingface.co/Kim2091/UltraSharp/resolve/main/4x-UltraSharp.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Z-Image** (13 nodes)
- **Z-Image** (13 nodes)
- **Z-Image** (13 nodes)
- **Z-Image** (13 nodes)
- **Z-Image** (13 nodes)
- **Optimized First-Last-Frame to Video** (3 nodes)
- **Optimized First-Last-Frame to Video** (3 nodes)
- **Optimized First-Last-Frame to Video** (3 nodes)
- **Optimized First-Last-Frame to Video** (3 nodes)
- **Optimized First-Last-Frame to Video** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 11 |  |
| `KSampler` | 10 | comfy-core |
| `LoraLoaderModelOnly` | 10 | comfy-core |
| `VAEDecode` | 10 | comfy-core |
| `GeminiNodeV3` | 6 |  |
| `CLIPTextEncode` | 5 | comfy-core |
| `ConditioningZeroOut` | 5 | comfy-core |
| `EmptySD3LatentImage` | 5 | comfy-core |
| `GetVideoComponents` | 5 |  |
| `ImageBatchMulti` | 5 |  |
| `ImageResizeKJv2` | 5 | comfyui-kjnodes |
| `ImageUpscaleWithModelBatched` | 5 |  |
| `ImpactStringSelector` | 5 |  |
| `KlingFirstLastFrameNode` | 5 |  |
| `ModelSamplingAuraFlow` | 5 | comfy-core |
| `PreviewImage` | 5 |  |
| `SaveImage` | 5 |  |
| `SaveVideo` | 5 |  |
| `UpscaleModelLoader` | 5 |  |
| `VAEEncode` | 5 |  |
| `PrimitiveInt` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `VHS_VideoCombine` | 1 |  |

## Notes embedded in the workflow

<details><summary>Model links</summary>

## Model links (when running locally)

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)


**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)


**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)


**upscale_model**

- [4x-UltraSharp.pth](https://huggingface.co/lokCX/4x-Ultrasharp/blob/main/4x-UltraSharp.pth)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_turbo_bf16.safetensors
│   └── 📂 vae/
│   │      └── ae.safetensors
│   └── 📂 upscale_models/
│          └── 4x-UltraSharp.pth
```

</details>

<details><summary>Read me!</summary>

```text
Load an image, hit run and be surprised by a new loop each time!

This is an hybrid workflow. It is using local models and API nodes.

You can use Z-Image LoRAs in the Z-Image Subgraphs.

You can bypass the save frames and save videos groups to only output the final combined video.

Enjoy,
Julien | MJM
```

</details>
