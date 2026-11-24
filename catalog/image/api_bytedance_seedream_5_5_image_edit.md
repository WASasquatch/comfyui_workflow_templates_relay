# Seedream 5.5: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_image_edit-1.webp" width="360" alt="Seedream 5.5: Image Edit api_bytedance_seedream_5_5_image_edit-1.webp">

> Upload an image and a text prompt to edit it. The result keeps the source resolution: the workflow reads the size from the input picture, so the edited image comes back at the same width and height.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_5_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream_5_5_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Seedream 5.5 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-11-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.0 |
| Usage | 2243 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | api_bytedance_seedream_5_5_image_edit_input.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `ByteDanceSeedreamNodeV3` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Seedream 5.5 Image Edit

**Input Assets**
- `api_bytedance_seedream_5_5_image_edit_input.png` — source portrait

Edit a picture with Seedream 5.5 through the partner API: state what changes, repeat what must stay. The node accepts two reference images; the first one is wired here.

1. **Load image** — the source picture.
2. **Edit** — the prompt names the changes (chocolate → macaron, hair, earrings, top, background) and restates the invariants (face, smile, pose, hand, framing).
3. **Compare / Save** — the result sits next to the input.

**Size** — the output keeps the source resolution: `Get Image Size` feeds the node's width and height, so a 1024×1024 picture comes back at 1024×1024. See the size note beside the canvas for preset sizes.

</details>

<details><summary>Note: Size</summary>

**Size — custom, taken from the input image**

`Get Image Size` reads the loaded picture and feeds `Size preset = Custom` plus that exact width and height, so the edit keeps the source resolution and aspect ratio.

To use a recommended size instead:
1. Delete the `Get Image Size` node (its width/height links disappear with it).
2. Pick a preset in `Size preset`, e.g. `(1K) 1024x1024 (1:1)`, `(1.5K) 1328x1776 (3:4)`, `(2K) 2048x2048 (1:1)`.
3. Or keep `Custom` and type `width` / `height` yourself.

A preset re-composes the canvas at that size; the edit still follows the source picture.

</details>
