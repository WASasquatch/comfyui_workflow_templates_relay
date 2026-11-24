# Ming Image 0.1 Design: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_ming_image_01_design_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_image_edit-1.webp" width="360" alt="Ming Image 0.1 Design: Image Edit image_ming_image_01_design_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_image_edit-2.webp" width="360" alt="Ming Image 0.1 Design: Image Edit image_ming_image_01_design_image_edit-2.webp">

> Edit an existing image with Ming Image 0.1 Design, a 6B model tuned for UI, infographics, and posters. It takes one input image plus the boxes you draw on it — position, description, and colour palette — and rebuilds them into a layer-by-layer caption, returning one re-rendered image. Ideal for restaging a layout, poster-style re-renders, and turning a photograph into a designed composition.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_ming_image_01_design_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_ming_image_01_design_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Ming Image |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-09-29 |
| Author | ComfyUI |
| Download size | 24.2 GB |
| Min ComfyUI version | 0.38.0 |
| Usage | 34 |
| Nodes | 96 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #49 | image | yellow_arch_daisy_field.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ming_image_0.1_design_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors) |
| `ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors) |
| `ming_image_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/vae/ming_image_vae_bf16.safetensors) |

## Subgraphs

- **Image Edit (Ming Image 0.1 Design)** (15 nodes)
- **Aspect Ratio (gcd-reduced)** (14 nodes)
- **Ideogram JSON to Ming Caption** (51 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RegexExtract` | 15 |  |
| `ComfyMathExpression` | 9 |  |
| `StringFormat` | 9 |  |
| `RegexReplace` | 8 |  |
| `MarkdownNote` | 6 |  |
| `CreateList` | 5 |  |
| `GetItemFromList` | 5 |  |
| `ComfyNumberConvert` | 4 |  |
| `PreviewAny` | 3 |  |
| `EndLoop` | 2 |  |
| `ImageStitch` | 2 |  |
| `PreviewImage` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `StartLoop` | 2 |  |
| `BasicGuider` | 1 |  |
| `BasicScheduler` | 1 |  |
| `BuildJsonPromptIdeogram` | 1 |  |
| `CLIPLoader` | 1 |  |
| `ConvertArrayToString` | 1 |  |
| `ConvertDictionaryToString` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `GetImageSize` | 1 |  |
| `LoadImage` | 1 |  |
| `ModelAttentionBackend` | 1 |  |
| `ModelSamplingFlux` | 1 |  |
| `RandomNoise` | 1 |  |
| `ResizeImageMaskNode` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SamplerLCM` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `StringLength` | 1 |  |
| `TextEncodeMingImageEdit` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Resize Input</summary>

Select and press Ctrl-B to enable `Resize Image/Mask` node if your input image is too large (over 2048*2048).

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [yellow_arch_daisy_field.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/yellow_arch_daisy_field.png)

## Model Links

- [Hugging Face:Comfy-Org/Ming-Image](https://huggingface.co/Comfy-Org/Ming-Image)

### Alternative Repos

- [ModelScope:Comfy-Org/Ming-Image](https://modelscope.cn/models/Comfy-Org/Ming-Image)

**diffusion_models**

- [ming_image_0.1_design_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors) (5.75 GB)

**vae**

- [ming_image_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/vae/ming_image_vae_bf16.safetensors) (242.1 MB)

**text_encoders**

- [ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors) (18.17 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── ming_image_0.1_design_int8_convrot.safetensors
│   ├── 📂 vae/
│   │   └── ming_image_vae_bf16.safetensors
│   └── 📂 text_encoders/
│       └── ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Ming Image 0.1 Design — Edit (subgraph + prompt)</summary>

# Ming Image 0.1 Design — Edit (ComfyUI)

Ming Image 0.1 **Design** (inclusionAI / Ant Ling): text-to-image and image editing with one checkpoint.
Files — see *Note: Model Links*.

Links — [Ming-Image repo](https://github.com/inclusionAI/Ming-Image) · [model card](https://huggingface.co/inclusionAI/Ming-Image-0.1-Design) · [Design skill](https://github.com/inclusionAI/ling-cookbook/tree/main/resources/recommended-skills/ling-ui-design) · [PPT skill](https://github.com/inclusionAI/ling-cookbook/tree/main/resources/recommended-skills/image-to-editable-ppt)

## Three subgraphs — double-click any of them to open

| subgraph | what it does |
|---|---|
| **Image Edit (Ming Image 0.1 Design)** | the model: reference image(s) + `prompt` → sample → decode |
| **Ideogram JSON → Ming Caption** | rewrites the Ideogram JSON + the bounding boxes into Ming's Figma-style caption and feeds `prompt` |
| **Aspect Ratio (gcd-reduced)** | nested inside the one above: `width` / `height` → `7:9, 896 × 1152 px` for `canvas_settings.aspect_ratio` |

## Image Edit subgraph parameters

| parameter | what it does |
|---|---|
| `image_1` … `image_8` | reference image(s) to edit; only `image_1` is required |
| `prompt` | the instruction (see below) |
| `width` / `height` | output size, wired from `Get Image Size` |
| `noise_seed` / `scheduler` / `steps` | sampling; default `simple`, 12 steps |
| `unet_name` / `vae_name` / `type` | weights, and text-encoder family (`qwen_image`) |
| `model_attention_backend` | `comfy kitchen attention` (INT8, fastest) is only listed on GPUs that support it — NVIDIA cc 7.5+ or AMD/ROCm; otherwise pick `pytorch attention`: same result, slower |

No negative prompt, no CFG — positive conditioning only.

## Prompt: 

**1 · Natural language**: you can disconnect the `Ideogram JSON to Ming Caption` output, then use your own prompt to edit the image

**2 · Ming's own Figma-style caption**: Currently this workflow builds a prompt that matches Ming's Figma-style caption, you can use it for precise control (same shape as the official [rewriter system prompt](https://github.com/inclusionAI/Ming-Image/blob/main/assets/t2i_rewriter_system_prompt.txt) emits):

```json
{
  "canvas_settings": {"aspect_ratio": "…", "ambient_lighting": "…", "image_style": "…"},
  "layers": [{"description": "…", "coordinates": "cx: 0.500, cy: 0.500, w: 1.000, h: 1.000",
              "hierarchy_and_relation": "…", "color_specs": ["#RRGGBB"]}]
}
```

Two keys only; `layers` runs background → topmost; `coordinates` is one string (centre + size, normalised); rendered text is quoted and owned once. `aspect_ratio` and the pixel size are computed from the boxes' canvas, so adding boxes or swapping the input image needs no edits. Example: [t2i_four_seasons_cabin_prompt.json](https://github.com/inclusionAI/Ming-Image/blob/main/assets/t2i_four_seasons_cabin_prompt.json)

</details>

<details><summary>MarkdownNote</summary>

If you can't find the editor on the node canvas, please make sure you have enabled Nodes 2.0 to see the editor

</details>

<details><summary>Note: Aspect ratio (gcd-reduced)</summary>

**Aspect ratio is computed, not typed**

`canvas_settings.aspect_ratio` must read like `7:9, 896 × 1152 px`. This nested subgraph derives it from the `width` / `height` its parent receives from `Get Image Size`:

* the loop count is computed as well — `ceil(1.5 * log2(max(width, height))) + 2` is an upper bound on the Euclidean steps (18 for 896 x 1152, 23 at the 16384 px maximum), so nothing here is hand-typed;
* inside the loop `r = a mod b`, then `a = b`; once `b` reaches 0 the first value freezes at `gcd(width, height)`;
* `width / gcd` and `height / gcd` become `ratio, width × height px` in `Format Text (canvas aspect ratio + pixels)`.

Swap the input image or resize the canvas and the ratio follows automatically.

</details>

<details><summary>Note: Ideogram JSON → Ming caption (built-in nodes only)</summary>

**What this subgraph does**

Turns the Ideogram JSON + the bounding boxes into Ming's own Figma-style caption (`canvas_settings` + `layers`) and sends it to the `prompt` of **Image Edit (Ming Image 0.1 Design)**.

| input | comes from | carries |
|---|---|---|
| `ideogram` | `Build JSON Prompt (Ideogram)` | the Ideogram JSON (style / lighting / background / palette …) |
| `elements` | `Create Bounding Boxes` → `elements` | the boxes, turned into the text queue the loop eats one item per iteration |
| `width` / `height` | `Get Image Size` | output size; the nested **Aspect Ratio (gcd-reduced)** subgraph turns them into `7:9, 896 × 1152 px` |

Output: `caption` → `prompt` of the Image Edit subgraph, plus the preview in `Preview as Text`.

**How the loop works**

One iteration per box. `Start Loop` runs `count` times, where `count` is the number of boxes — counted on the left by `Replace Text (Regex)` + `Text Length` (that count is wired into the loop's `max_iteration`, so adding or removing boxes needs no rewiring). Each iteration:

* pulls the next box JSON out of the queue,
* maps `bbox [ymin, xmin, ymax, xmax]` → `cx: …, cy: …, w: …, h: …` (normalised centre + size),
* `desc` → `description`, `color_palette` → `color_specs`, a text box becomes `Text layer reading "…"`,
* appends the layer and drops that box from the queue.

The base layer ("the whole canvas") is the loop's seed; layers accumulate background → topmost.

**To skip this subgraph**

Bypass it (`Ctrl+B`) and either type English into `prompt`, or wire `Build JSON Prompt (Ideogram)` straight into `prompt` to send the Ideogram JSON instead of the Ming caption.

</details>
