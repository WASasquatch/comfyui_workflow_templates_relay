# Exploded View Animation

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_exploded_view-1.webp" width="360" alt="Exploded View Animation template_eric_exploded_view-1.webp">

> Upload an image of a device or object to generate start and end frames. The workflow animates the transition to an exploded view and back, outputting a seamless video loop.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_exploded_view.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_eric_exploded_view.json)

## Details

| | |
|---|---|
| Name | `template_eric_exploded_view` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Nano Banana 2, Seedance 2.0 |
| Tags | API, FLF2V, Video |
| Type | API |
| Date | 2026-03-06 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.26.2 |
| Usage | 22 |
| Nodes | 16 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #29 | image | template_eric_exploded_view_first_frame.png |
| output | `SaveVideo` #381 | video | template_eric_exploded_view.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 3 | comfy-core |
| `ByteDance2FirstLastFrameNode` | 2 |  |
| `GeminiNanoBanana2V2` | 2 |  |
| `GetVideoComponents` | 2 | comfy-core |
| `Note` | 2 |  |
| `SaveImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
In the prompt area describe the object/device is. The system prompt is already describing what it should be doing so no need to tell it to explode anything.
```

</details>

<details><summary>Note</summary>

```text
This will allow you to stitch the videos together, but it will not output audio. If you need audio, you can save the individual generations and combine them later using a video editing tool.
```

</details>
