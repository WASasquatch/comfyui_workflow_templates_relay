# AnimateDiff - IPAdapters Looping Animation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_purz_animatediff_simple_weighted_ipadapters_looping_animation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_animatediff_simple_weighted_ipadapters_looping_animation-1.webp" width="360" alt="AnimateDiff - IPAdapters Looping Animation templates_purz_animatediff_simple_weighted_ipadapters_looping_animation-1.webp">

> Drag and drop then dream through a stack of images

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_animatediff_simple_weighted_ipadapters_looping_animation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_purz_animatediff_simple_weighted_ipadapters_looping_animation.json)

## Details

| | |
|---|---|
| Name | `templates_purz_animatediff_simple_weighted_ipadapters_looping_animation` |
| Category | Foundation › Video |
| Output | video |
| Models | SD1.5 |
| Tags | Video, Image to Video |
| Type | open source |
| Date | 2026-03-04 |
| Author | PurzBeats |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 13 |
| Nodes | 36 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #61 | image | animatediff-weighted_ipadapters-input1.png |
| input | `LoadImage` #63 | image | animatediff-weighted_ipadapters-input2.png |
| input | `LoadImage` #65 | image | animatediff-weighted_ipadapters-input3.png |

## Custom nodes required

- [comfyui-animatediff-evolved](https://registry.comfy.org/nodes/comfyui-animatediff-evolved)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_ipadapter_plus](https://registry.comfy.org/nodes/comfyui_ipadapter_plus)

## Subgraphs

- **AnimateDiff IPA Weighted Batches** (18 nodes)
- **Result Grid** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageScaleToTotalPixels` | 3 |  |
| `ImageStitch` | 3 |  |
| `LoadImage` | 3 |  |
| `RepeatImageBatch` | 3 |  |
| `ADE_MultivalDynamic` | 2 |  |
| `CLIPTextEncode` | 2 |  |
| `IPAdapterBatch` | 2 |  |
| `MarkdownNote` | 2 |  |
| `VHS_VideoCombine` | 2 |  |
| `ADE_AnimateDiffSamplingSettings` | 1 |  |
| `ADE_ApplyAnimateDiffModelSimple` | 1 |  |
| `ADE_LoadAnimateDiffModel` | 1 |  |
| `ADE_LoopedUniformContextOptions` | 1 |  |
| `ADE_UseEvolvedSampling` | 1 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `GetImageSizeAndCount` | 1 |  |
| `ImageBatchMulti` | 1 |  |
| `IPAdapterUnifiedLoader` | 1 |  |
| `IPAdapterWeights` | 1 |  |
| `KSampler` | 1 |  |
| `PatchModelAddDownscale` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>🌀 Simple Weighted IPAdapters AnimateDiff Workflow</summary>

### Overview
Use this workflow to create smooth animated transitions between multiple images using **Weighted IPAdapters** and **AnimateDiff**.

### Steps
1. **Add images to the Batch node** — these will “flow” sequentially through the animation.  
2. **Loop the animation** by connecting the *first image* to both the **first** and **last** input slots on the Batch node.

### Parameters
| Setting | Description |
|----------|-------------|
| **width** | Target output width (in pixels). |
| **height** | Target output height (in pixels). |
| **frames_per_image** | Number of frames the animation “holds” on each image before transitioning. |
| **prompt** | Describe what you'd like to see in the transformation between images
| **noise_type** | Experiment with different noise types to get different kinds of animations

</details>

<details><summary>MarkdownNote</summary>

### Explanation

In this part of the workflow:

1. **Frame Calculation**  
   We begin by getting the **total number of frames** from the final output.  
   This number determines how long each image should “sit” on screen before transitioning.

2. **Image Repetition**  
   Each image in the batch is **repeated** according to the total frame count, ensuring all images align with the animation length.

3. **Horizontal Stitch (Top Three Images)**  
   The **top three images** are combined using **Image Stitch** nodes set to `Right`.  
   This places the images side-by-side horizontally, forming a single wide composite frame.

4. **Vertical Stitch (Final Grid and Video Output)**  
   The **three horizontally stitched images** and the **final video** are then merged using **Image Stitch** nodes set to `Down`.  
   This stacks each horizontal strip vertically, creating the final **image grid** used for output.

</details>
