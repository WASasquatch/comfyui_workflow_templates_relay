# Kling 4.0: Long Image (Webpage)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_long_image-1.webp" width="360" alt="Kling 4.0: Long Image (Webpage) api_kling4_long_image-1.webp">

> Generate one very tall image that reads as a finished web page: header, hero, content bands and footer laid out in a single pass. Describe the page band by band and state the language of the copy.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_long_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_long_image.json)

## Details

| | |
|---|---|
| Name | `api_kling4_long_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kling, Kling 4.0 |
| Tags | API, Image, Long Image, Web Design |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 0 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #4 | image | api_kling4_long_image_webpage.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4LongImageNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Kling 4.0: Long Image (webpage)

Generates **one extremely tall image** (roughly 1:10) that reads as a finished web page, in a single pass — header, hero, content bands and footer laid out together rather than stitched from separate generations.

### How the node works

- `skill` picks the layout template. **`webpage`** (this workflow) designs a page from text; `ecommerce` instead takes 1–3 product photos and produces a product detail page.
- `prompt` is the art direction **and** the structure: describe the page band by band, top to bottom, and say explicitly what must not appear (e.g. *no search field, no filter chips, no product grid*). Without that, the model drifts toward a generic shop or corporate site.
- Optional inputs on `webpage`: `style_image` (referenced as `@Image1`, supplies look and layout language) and `subject_image` (`@Image2`, a subject the page is built around). You can run it fully text-only.
- `resolution` is `1K` or `2K` only — there is no aspect-ratio control, the page shape is derived by the endpoint.
- `length` exists only for `ecommerce` (short / medium / long); the webpage skill ignores it.

### What a long image is like

- Output is enormous and thin: expect something like **2048 × 16500** at 2K, up to ~50k pixels tall at the longest ecommerce length. Open the file in an image viewer, never assume it fits a screen.
- The layout is coherent — one grid, consistent type scale, real negative space — which is what makes it useful as a design artifact rather than a collage.
- **Text inside the image is rendered by the model**: short display type and prices usually come out clean, long body copy and CJK paragraphs do not. Treat all copy as placeholder art, not as content to ship.
- The ecommerce skill is a fixed vendor script (hero → benefits → fabric detail → specs → care). It tends *not* to render prices, size tables or a footer even when asked; the webpage skill follows a described structure more loosely than a literal list.
- Generation is slow for an image model — 1–5 minutes per page, the 2K long ecommerce case being the slowest.

### When to use it

- **Landing-page and site design drafts** — several directions to compare before anything is coded; hand the winner to a designer or an agent as a layout reference.
- **Brand and campaign pages** — a full visual narrative in one artifact instead of a folder of slices.
- **E-commerce PD page mockups** — feed product photos, get the skeleton of a detail page.
- **App or onboarding flow sketches** — one tall canvas where each band is a screen.

### Tips

- Ask for the band order explicitly, and state the language (*"All visible text must be in English only"*) — it otherwise defaults to Chinese.
- Keep the page copy short in the prompt; describe imagery and layout, not paragraphs.
- Crop the top 2000 px for a quick look instead of opening a 20k-pixel file.

</details>
