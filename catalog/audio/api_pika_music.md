# Pika Music: Text to Music

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_music-1.webp" width="360" alt="Pika Music: Text to Music api_pika_music-1.webp">

> Turn a style description and optional lyrics into a finished song with Pika Music through the partner API, no weights to download. Write the arrangement, mood and instrumentation into the prompt, add section-tagged lyrics such as [Verse] and [Chorus] for a vocal track, or leave them empty for an instrumental, and pick any length from 10 to 360 seconds; the same node switches to a cover mode that restyles an uploaded song at its original length. Ideal for trailers, jingles and background tracks on a machine without a GPU.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_music.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pika_music.json)

## Details

| | |
|---|---|
| Name | `api_pika_music` |
| Category | Foundation › Audio |
| Media type | image |
| Models | Pika |
| Tags | API, Audio, Text to Music |
| Type | API |
| Date | 2026-11-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.3 |
| Usage | 56 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveAudioAdvanced` #2 | audio | api_pika_music.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PikaMusicNode` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 | comfy-core |
