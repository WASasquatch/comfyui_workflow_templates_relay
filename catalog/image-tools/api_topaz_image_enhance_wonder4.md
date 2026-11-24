# Image Upscale: Topaz Wonder 4

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_image_enhance_wonder4)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder4-1.webp" width="360" alt="Image Upscale: Topaz Wonder 4 api_topaz_image_enhance_wonder4-1.webp">

> Upscale a soft, compressed image with Topaz's Wonder 4 generative model: it rebuilds plausible detail instead of stretching pixels, keeping torn edges, seams and flat color fields intact at 1x to 6x. The workflow takes 1 input image and produces 1 enhanced output next to a side-by-side comparison. Ideal for collage, illustration and graphic work that needs to survive a small or compressed source.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder4.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_image_enhance_wonder4.json)

## Details

| | |
|---|---|
| Name | `api_topaz_image_enhance_wonder4` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 135 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | topaz_wonder4_collage_lowres.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageScaleBy` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TopazImageEnhanceV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Topaz Wonder 4: Image Upscale

**Bring a small, soft image back.** Wonder 4 rebuilds plausible detail instead of stretching pixels, so a soft, lightly compressed copy returns clean at 2 to 6 times its size.

---

### What this graph does

1. **Load Image**: the small, soft source. The bundled demo is a 512 x 512, lightly compressed copy of a 1024 x 1024 paper-collage image.
2. **Image Scale By**: sets the target. `scale_by` 2 means twice the input, so the demo comes back at the original 1024 x 1024.
3. **Image Size**: reads that scaled size and passes it to the node as `output_width` and `output_height`.
4. **Topaz Image Enhance** with `model` set to `Wonder 4`: upscales to the target size.
5. **Save Image (Advanced)** writes the result, **Compare Images** shows the soft input next to it.

---

### Controls

| Control | What it does |
|---|---|
| `model` | `Wonder 4` is a single pass at the target size. `Wonder 3.5` and `Bloom 2` add their own settings, such as Low / Medium / High enhancement or a prompt |
| `scale_by` | Upscale factor: 1x to 6x on Wonder 4 and Wonder 3.5, up to 12x on Bloom 2 |
| `output_width` / `output_height` | Filled here from Image Size. Zero means automatic |
| `filename_prefix` | Where the result lands in the output folder |

Wonder keeps the source aspect ratio: when the requested width and height disagree, the larger scale wins and the output is bigger than asked. The node accepts up to 179 megapixels and 32000 pixels per side, and it downscales the input to about 16 megapixels before sending it.

### When Wonder 4 fits

Built for small, medium, soft, noisy or compressed images: old scans, screenshots, AI thumbnails, phone crops. A graphic, textured image is a good test, since torn edges, seams and flat color fields show at once whether the model invents detail or keeps the original. For an already sharp, high resolution photo a precision upscaler keeps more of the original.

</details>
