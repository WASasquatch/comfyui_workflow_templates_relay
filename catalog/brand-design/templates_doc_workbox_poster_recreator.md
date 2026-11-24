# Realistic Poster Redesign With Character Transformation

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_doc_workbox_poster_recreator-1.webp" width="360" alt="Realistic Poster Redesign With Character Transformation templates_doc_workbox_poster_recreator-1.webp">

> Transform uploaded images into realistic poster designs. Change character poses, faces, and clothing while maintaining artistic style and color schemes. Outputs a visually impactful poster with artistic typography.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_doc_workbox_poster_recreator.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_doc_workbox_poster_recreator.json)

## Details

| | |
|---|---|
| Name | `templates_doc_workbox_poster_recreator` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-03-21 |
| Author | Doc_workBox |
| Min ComfyUI version | 0.15.1 |
| Usage | 10 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | reference_poster.png |
| output | `SaveImage` #4 | image | templates_doc_workbox_poster_recreator.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 1 |  |
| `GeminiImage2Node` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveImage` | 1 |  |
| `StringConcatenate` | 1 |  |

## Notes embedded in the workflow

<details><summary>Generate Mode</summary>

## On_false: Poster remake mode
Enter the content you want on the new poster
## On_true: Image edit mode
Regular image edit

</details>
