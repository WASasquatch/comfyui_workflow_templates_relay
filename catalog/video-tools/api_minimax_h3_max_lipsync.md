# Lip Sync: MiniMax H3 Max

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_max_lipsync)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_lipsync-1.webp" width="360" alt="Lip Sync: MiniMax H3 Max api_minimax_h3_max_lipsync-1.webp">

> Animate a portrait from an audio track with MiniMax H3 Max lip sync. Connect one image and one voice clip and the model renders the performance, matching the mouth to the audio and keeping the length of the recording, at 480P to 2K. An optional transcription pass steers the mouth shapes with the spoken text. Ideal for talking-head ads, narration and dubbing a still portrait.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_lipsync.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_lipsync.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_lipsync` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, Lip Sync, Video |
| Type | API |
| Date | 2026-11-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 105 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | api_minimax_h3_max_lipsync_input.png |
| input | `LoadAudio` #2 | audio | api_minimax_h3_max_lipsync_audio.mp3 |
| output | `SaveVideo` #4 | video | api_minimax_h3_max_lipsync.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MinimaxHailuo03MaxLipSyncNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Lip Sync: MiniMax H3 Max

**Make a still portrait talk.** Give the node a face and a voice track and it animates the mouth to the audio, keeping the rest of the frame still. The clip comes back exactly as long as the audio.

**Input Assets:**
- [api_minimax_h3_max_lipsync_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_minimax_h3_max_lipsync_input.png)
- [api_minimax_h3_max_lipsync_audio.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_minimax_h3_max_lipsync_audio.mp3)
---

### What this graph does

1. **Load Image**: the portrait to animate, at least 256 x 256, aspect ratio between 0.4 and 2.5.
2. **Load Audio**: the voice track, 5 to 899 seconds.
3. **MiniMax H3 Max Lip Sync**: animates the mouth to the audio.
4. **Save Video**: writes the MP4.

---

### Controls

| Control | What it does |
|---|---|
| `model` | `MiniMax H3 Max` is the only option on this node |
| `resolution` | `480P`, `768P`, `1080P` or `2K`, default `768P`. The output aspect ratio is the supported one nearest to the image |
| `transcription` | Transcribes the audio first to guide the lip sync. Off by default; on in this graph |
| `seed` | Same audio and seed give similar, not identical, results |

---

### Gotchas

- The audio must be at least 5 seconds. A 4.4 second line is rejected before generation, so pad the tail or use a longer take.
- Output length equals audio length, and there is no duration widget. Trim the audio to the length you want the clip to be.
- The output is a talking portrait, not a full performance: hands, camera moves and background action are not driven by the audio.
- Pick a portrait that is already lit the way you want it. The node animates the mouth, it does not relight the shot.

</details>
