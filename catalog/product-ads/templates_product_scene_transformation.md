# Product Scene Transformation

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_product_scene_transformation-1.webp" width="360" alt="Product Scene Transformation templates_product_scene_transformation-1.webp">

> Upload a product video and generate a dynamic product scene transformation using Nano Banana Pro & Wan VACE 2.1

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_product_scene_transformation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_product_scene_transformation.json)

## Details

| | |
|---|---|
| Name | `templates_product_scene_transformation` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Kling, Nano Banana Pro, Wan |
| Tags | API, Style Transfer, Video |
| Type | API |
| Date | 2026-02-10 |
| Author | sirolim |
| Download size | 45.5 GB |
| Min ComfyUI version | 0.15.0 |
| Usage | 17 |
| Nodes | 99 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #108 | image | comfy_sofa.png |
| output | `SaveVideo` #126 | video | templates_product_scene_transformation_control_video.mp4 |
| output | `SaveVideo` #125 | video | templates_product_scene_transformation_output.mp4 |
| output | `SaveImage` #134 | image | templates_product_scene_transformation_style_reference.png |

## Custom nodes required

- [comfyui-depthanythingv2](https://registry.comfy.org/nodes/comfyui-depthanythingv2)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [Kosinkadink/ComfyUI-DownloadWhatIWant](https://registry.comfy.org/nodes/Kosinkadink/ComfyUI-DownloadWhatIWant)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors) |
| `umt5_xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Wan 2.1 VACE** (10 nodes)
- **Wan 2.1 VACE** (10 nodes)
- **Wan 2.1 VACE** (10 nodes)
- **Wan 2.1 VACE** (10 nodes)
- **Select Images** (5 nodes)
- **Crop Images** (20 nodes)
- **Product Scene Transformation** (29 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 10 | comfyui_essentials |
| `CLIPTextEncode` | 8 | comfy-core |
| `ImageFromBatch` | 8 | comfy-core |
| `ImageRemoveAlpha+` | 5 | comfyui_essentials |
| `CLIPLoader` | 4 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `KSampler` | 4 | comfy-core |
| `LoraLoaderModelOnly` | 4 | comfy-core |
| `Reroute` | 4 |  |
| `TrimVideoLatent` | 4 | comfy-core |
| `UNETLoader` | 4 | comfy-core |
| `VAEDecode` | 4 | comfy-core |
| `VAELoader` | 4 | comfy-core |
| `WanVaceToVideo` | 4 | comfy-core |
| `PrimitiveInt` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `SaveVideo` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `CM_IntToFloat` | 1 | Kosinkadink/ComfyUI-DownloadWhatIWant |
| `CreateVideo` | 1 | comfy-core |
| `DepthAnything_V2` | 1 | comfyui-depthanythingv2 |
| `DownloadAndLoadDepthAnythingV2Model` | 1 | comfyui-depthanythingv2 |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageRangeFromBatch` | 1 | comfyui-kjnodes |
| `GetImageSize` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageRemoveBackground+` | 1 | comfyui_essentials |
| `ImageResize+` | 1 | comfyui_essentials |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `KlingVideoNode` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `RemBGSession+` | 1 | comfyui_essentials |
| `ResizeAndPadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `VHS_SelectEveryNthImage` | 1 | comfyui-videohelpersuite |

## Notes embedded in the workflow

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**diffusion_models**

- [wan2.1_vace_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) (32.29 GB)

**text_encoders**

- [umt5_xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) (10.59 GB)

**loras**

- [lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors) (2.38 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**depthanything**

- [depth_anything_v2_vitl_fp32.safetensors](https://huggingface.co/Kijai/DepthAnythingV2-safetensors/resolve/main/depth_anything_v2_vitl_fp32.safetensors) (1.25 GB)

**Custom Nodes** (Please add download links manually)

*depthanything/* (from custom node loaders)
- depth_anything_v2_vitl_fp32.safetensors (DownloadAndLoadDepthAnythingV2Model): [Add link here]

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── wan2.1_vace_14B_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp16.safetensors
│   ├── 📂 loras/
│   │   └── lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
│   ├── 📂 vae/
│   │   └── wan_2.1_vae.safetensors
│   └── 📂 depthanything/
│       └── depth_anything_v2_vitl_fp32.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>How to use</summary>

## Input Asset

- [comfy_sofa.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/comfy_sofa.png)

Upload a product image and update the corresponding prompt

This workflow first generates a product video and then, by modifying specific frames, switches between different scenes in a continuous sequence.

</details>
