# VEED Dubbing: Video Translation

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_dubbing-1.webp" width="360" alt="VEED Dubbing: Video Translation api_veed_dubbing-1.webp">

> Translate the speech in a video into another language with VEED Dubbing: each speaker's voice is cloned and their lips are re-synced to the translation. Pick between the cheaper standard tier and pro, which adds regional accents and stereo audio. Built for footage with a visible face and a talk track.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_dubbing.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_dubbing.json)

## Details

| | |
|---|---|
| Name | `api_veed_dubbing` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | VEED |
| Tags | API, Video |
| Type | API |
| Date | 2026-10-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.1 |
| Usage | 41 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | api_veed_dubbing_input_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `VeedDubbingNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# VEED Dubbing

**Translate the speech in a video into another language.** Every speaker's voice is cloned and their lips are re-synced
to the translation, so the result looks spoken in the target language rather than captioned. Partner (API) node: it runs
on Comfy's servers, needs an account, and nothing is rendered locally.

## Input Asset

- [api_veed_dubbing_input_video.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_veed_dubbing_input_video.mp4)

## Requirements

- **The audio must contain voice that can be converted.** Narration, dialogue or an interview all work; music, sound
  effects or silence give the model nothing to translate.
- **There must be a face in the video.** Dubbing works on what it can see - a single speaker facing the camera is the
  reliable case. Backs of heads, hands, product shots and crowd scenes do not dub.

## How to use it

- `model`: `standard` is the cheaper tier with mono audio (Spanish is Latin American, Portuguese is Brazilian);
  `pro` adds regional accents and stereo audio.
- `target_language`: 85 languages on standard, 101 options on pro (regional variants such as `English (UK)` or
  `Chinese (Taiwan)`).
- `source_language`: leave it on `auto` unless the model mishears the original; naming the spoken language improves
  accuracy on short clips and strong accents.
- `seed` only decides whether the node re-runs - the result is non-deterministic either way.

## Limits

- Up to 599 seconds of video. The output is as long as its audio track and plays at 25 fps, so a 24 fps source becomes
  25 fps.
- One speaker is the reliable case. Multi-speaker footage is supported but voice assignment can drift.
- No subtitle file is produced: the node returns a dubbed video only.

</details>
