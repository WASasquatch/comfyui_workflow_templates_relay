# YouTube Thumbnail Generator

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_thumbnail_generator-1.webp" width="360" alt="YouTube Thumbnail Generator template_eric_thumbnail_generator-1.webp">

> Generate high-contrast, clickable YouTube thumbnails using Nano Banana Pro. Creates dramatic compositions with exaggerated subjects and bold color strategies for maximum engagement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_thumbnail_generator.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_eric_thumbnail_generator.json)

## Details

| | |
|---|---|
| Name | `template_eric_thumbnail_generator` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-03-21 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.20.3 |
| Usage | 9 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | man_with_dog.png |
| output | `SaveImage` #9 | image | ComfyUI_00223_.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BatchImagesNode` | 1 |  |
| `GeminiNanoBanana2` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Enable multi-image input</summary>

Select the `Batch Images` node and press Ctrl-B to enable it. Then, add more load image nodes to provide input images.

</details>

<details><summary>Note</summary>

```text
Add an image as a reference for the main subject or object you want in the thumbnail. You can include multiple reference images, like another thumbnail, to help guide the style. Enable batch image mode and copy/paste the Load Image node into Image 1. This makes it easy to keep adding more reference images as needed.
```

</details>
