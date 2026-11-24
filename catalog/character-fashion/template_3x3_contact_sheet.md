# 3x3 Contact Sheet

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_3x3_contact_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_3x3_contact_sheet-1.webp" width="360" alt="3x3 Contact Sheet template_3x3_contact_sheet-1.webp">

> Generate a 3x3 grid of image variations from a simple prompt and reference image using Nano Banana. 
> 
> Pick your favorite frame from the grid, then recreate it as a standalone high-quality image while maintaining character and outfit consistency.
> 
> Great for concept exploration, pose variations, camera angles, outfit ideas, and fast visual inspiration without generating each image individually.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_3x3_contact_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_3x3_contact_sheet.json)

## Details

| | |
|---|---|
| Name | `template_3x3_contact_sheet` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Nano Banana 2 |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-05-21 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.20.3 |
| Distributions | cloud |
| Usage | 15 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #86 | image | man_3x3_contact_sheet.png |
| input | `LoadImage` #88 | image | input_3x3_contact_sheet.png |
| input | `LoadImage` #89 | image | suit_3x3_contact_sheet.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 |  |
| `MarkdownNote` | 3 |  |
| `GeminiNanoBanana2V2` | 2 |  |
| `SaveImage` | 2 |  |
| `CustomCombo` | 1 |  |
| `StringReplace` | 1 |  |

## Notes embedded in the workflow

<details><summary>Model links</summary>

# 3x3 Contact Sheet Workflow Guide

This workflow is split into 3 main sections:

1. Main Contact Sheet Generator
2. Grid Image Loader
3. Individual Image Extraction Groups

The purpose of this workflow is to quickly generate multiple image ideas in a single 3x3 grid, then select one of those images to recreate in higher quality as an individual image.

---

</details>

<details><summary>Step 1</summary>

## Step 1 — Generate The Contact Sheet

Start by adding your subject reference image.

You can also optionally add additional reference images for:
- outfit consistency
- character consistency
- style references

Then enter a simple prompt describing your idea, concept, action, or scene.

You do not need to over-describe the prompt.  
The Nano Banana prompt node already expands and improves your input automatically.

Before running the workflow:

- Make sure the group called **Select Image** is bypassed
- Select the nodes in that group
- Press `Ctrl + B` to disable them

Then run the main contact sheet group to generate your 3x3 contact sheet with multiple variations of your concept.

</details>

<details><summary>Step 1</summary>

## Step 2 — Select And Generate An Image

After generating the contact sheet:

- Select all nodes in the **Select Image** group
- Press `Ctrl + B` again to remove bypass and enable the group.
- Bypass the `3x3 Contact Sheet` group so it doesn't run again but you may want to leave your `Subject` image node active so that the group below will see what the subject looks like.

Then:

1. Click the image selection area
2. Open:
   - `Inputs & Outputs`
   - then `Outputs`
3. Select the contact sheet you just generated

Next, go to the **Custom Combo Frame Mode** node.

Under the `Custom Combo` node, select the image position you want from the contact sheet:

- Top Left
- Top Center
- Top Right
- Middle Left
- Center
- Middle Right
- Bottom Left
- Bottom Center
- Bottom Right

Make sure the selected position matches the image you liked from the contact sheet.

Then run the workflow.

The workflow will isolate that frame and recreate it as a higher-quality standalone image.

## Notes

- If the result is slightly inaccurate, try generating again
- Occasionally the workflow may select the wrong part of the grid, but usually it matches correctly after another pass
- You can continue generating more variations from the same contact sheet
- Or bypass the selection group again and return to the main contact sheet generator to create a completely new grid of results

</details>
