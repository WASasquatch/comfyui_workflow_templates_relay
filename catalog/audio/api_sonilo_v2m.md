# Sonilo: Video Soundtrack Generation

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_sonilo_v2m)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_v2m-1.webp" width="360" alt="Sonilo: Video Soundtrack Generation api_sonilo_v2m-1.webp">

> Generate synchronized soundtracks from video footage. Input a video to produce music that matches its pacing and emotional cues, outputting a perfectly timed audio file.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_v2m.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_sonilo_v2m.json)

## Details

| | |
|---|---|
| Name | `api_sonilo_v2m` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Sonilo |
| Tags | API, Audio, Music |
| Type | API |
| Date | 2026-04-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 67 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #705 | video | leopard_rider.mp4 |

## Subgraphs

- **Video Audio Merger** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `AudioAdjustVolume` | 2 | comfy-core |
| `AudioMerge` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SoniloVideoToMusic` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Please make sure the input video contains audio. Otherwise, the subgraph above will not run.

</details>
