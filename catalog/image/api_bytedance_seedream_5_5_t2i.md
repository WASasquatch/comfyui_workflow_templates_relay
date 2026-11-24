# Seedream 5.5: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_t2i-1.webp" width="360" alt="Seedream 5.5: Text to Image api_bytedance_seedream_5_5_t2i-1.webp">

> Generate an image from a text prompt with Seedream 5.5 through the partner API, including typography and transparent backgrounds in the same pass. The demo sits at (1K) 1024x1024; any recommended size preset works.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_5_t2i.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream_5_5_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Seedream 5.5 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-11-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.0 |
| Usage | 738 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedreamNodeV3` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

## Seedream 5.5 — Text to Image

A prompt goes in, one image comes out. There is no input picture: the node calls the Seedream 5.5 API and returns what the prompt asks for.

- **Prompt** — subject, camera angle and light first, then the text you want inside the picture in quotes (`"SEEDREAM"`), and what to keep out (`no real mall logos`).
- **Size preset** — the demo uses `(1K) 1024x1024 (1:1)`. Pick another recommended size such as `(1.5K) 1328x1776 (3:4)` or `(2K) 2048x2048 (1:1)`, or choose `Custom` and type width and height yourself.
- **Seed** — fixed here so the card stays reproducible; switch to `randomize` for fresh variations.

Typography and transparent backgrounds render in the same pass, so posters and stickers need no second step.

</details>
