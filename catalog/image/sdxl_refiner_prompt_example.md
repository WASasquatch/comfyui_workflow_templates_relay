# SDXL Refiner Prompt

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=sdxl_refiner_prompt_example)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxl_refiner_prompt_example-1.webp" width="360" alt="SDXL Refiner Prompt sdxl_refiner_prompt_example-1.webp">

> Enhance SDXL images using refiner models.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxl_refiner_prompt_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/sdxl_refiner_prompt_example.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/)

## Details

| | |
|---|---|
| Name | `sdxl_refiner_prompt_example` |
| Category | Foundation › Image |
| Output | image |
| Models | SDXL, Stability |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 12.1 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 52 |
| Nodes | 20 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd_xl_base_1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true) |
| `sd_xl_refiner_1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Note` | 6 |  |
| `CLIPTextEncode` | 4 | comfy-core |
| `CheckpointLoaderSimple` | 2 | comfy-core |
| `KSamplerAdvanced` | 2 | comfy-core |
| `PrimitiveNode` | 2 |  |
| `EmptyLatentImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note - Load Checkpoint BASE</summary>

```text
This is a checkpoint model loader. 
 - This is set up automatically with the optimal settings for whatever SD model version you choose to use.
 - In this example, it is for the Base SDXL model
 - This node is also used for SD1.5 and SD2.x models
 
NOTE: When loading in another person's workflow, be sure to manually choose your own *local* model. This also applies to LoRas and all their deviations
```

</details>

<details><summary>Note - Load Checkpoint REFINER</summary>

```text
This is a checkpoint model loader. 
 - This is set up automatically with the optimal settings for whatever SD model version you choose to use.
 - In this example, it is for the Refiner SDXL model

NOTE: When loading in another person's workflow, be sure to manually choose your own *local* model. This also applies to LoRas and all their deviations.
```

</details>

<details><summary>Note - VAE Decoder</summary>

```text
This node will take the latent data from the KSampler and, using the VAE, it will decode it into visible data

VAE = Latent --> Visible

This can then be sent to the Save Image node to be saved as a PNG.
```

</details>

<details><summary>Note - Empty Latent Image</summary>

```text
This node sets the image's resolution in Width and Height.

NOTE: For SDXL, it is recommended to use trained values listed below:
 - 1024 x 1024
 - 1152 x 896
 - 896  x 1152
 - 1216 x 832
 - 832  x 1216
 - 1344 x 768
 - 768  x 1344
 - 1536 x 640
 - 640  x 1536
```

</details>

<details><summary>Note</summary>

```text
These can be used to control the total sampling steps and the step at which the sampling switches to the refiner.
```

</details>

<details><summary>Note - KSampler ADVANCED General Information</summary>

```text
Here are the settings that SHOULD stay in place if you want this workflow to work correctly:
 - add_noise: enable = This adds random noise into the picture so the model can denoise it

 - return_with_leftover_noise: enable = This sends the latent image data and all it's leftover noise to the next KSampler node.

The settings to pay attention to:
 - control_after_generate = generates a new random seed after each workflow job completed.
 - steps = This is the amount of iterations you would like to run the positive and negative CLIP prompts through. Each Step will add (positive) or remove (negative) pixels based on what stable diffusion "thinks" should be there according to the model's training
 - cfg = This is how much you want SDXL to adhere to the prompt. Lower CFG gives you more creative but often blurrier results. Higher CFG (recommended max 10) gives you stricter results according to the CLIP prompt. If the CFG value is too high, it can also result in "burn-in" where the edges of the picture become even stronger, often highlighting details in unnatural ways.
 - sampler_name = This is the sampler type, and unfortunately different samplers and schedulers have better results with fewer steps, while others have better success with higher steps. This will require experimentation on your part!
 - scheduler = The algorithm/method used to choose the timesteps to denoise the picture.
 - start_at_step = This is the step number the KSampler will start out it's process of de-noising the picture or "removing the random noise to reveal the picture within". The first KSampler usually starts with Step 0. Starting at step 0 is the same as setting denoise to 1.0 in the regular Sampler node.
 - end_at_step = This is the step number the KSampler will stop it's process of de-noising the picture. If there is any remaining leftover noise and return_with_leftover_noise is enabled, then it will pass on the left over noise to the next KSampler (assuming there is another one).
```

</details>

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/)

</details>
