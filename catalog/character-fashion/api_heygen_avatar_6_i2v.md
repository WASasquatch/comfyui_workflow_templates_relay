# HeyGen Avatar 6: Photo to Video

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_avatar_6_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_6_i2v-1.webp" width="360" alt="HeyGen Avatar 6: Photo to Video api_heygen_avatar_6_i2v-1.webp">

> Turn one photo and one voice track into a talking clip. HeyGen Avatar 6 keeps the photo's identity and scene, lip-syncs the performance to your audio and follows a motion prompt for gestures, expression, posture and camera. The clip runs the length of the audio, renders at 1080p or 2K, and can use Avatar 6 or the cheaper Avatar 6 Turbo. Ideal for giving a portrait a voice, making presenter clips without a shoot, and bringing character art to life.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_6_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_avatar_6_i2v.json)

## Details

| | |
|---|---|
| Name | `api_heygen_avatar_6_i2v` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | HeyGen Avatar 6 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.0 |
| Usage | 219 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | pink_hair_portrait.png |
| input | `LoadAudio` #2 | audio | avatar6_narration.mp3 |
| output | `SaveVideo` #4 | video | api_heygen_avatar_6_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `HeyGenAvatar6ReferenceToVideoNode` | 1 |  |
| `HeyGenTextToSpeechNode` | 1 |  |
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## HeyGen Avatar 6: Photo to Video

One photo plus one voice track becomes a talking clip. The photo carries the identity and the
scene, the AUDIO clip sets the length, and a motion prompt directs the performance.

## Input Assets

- [pink_hair_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pink_hair_portrait.png)
- [avatar6_narration.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/avatar6_narration.mp3)

### How to use

1. Sign in with your ComfyUI account. This is an API node, it bills per render.
2. Load a head-and-shoulders or half-body photo with the hands free — the model re-stages the
   pose, so a photo with the arms crossed or the hands on the face comes back re-posed.
3. Connect an AUDIO clip (1.5 s to 10 minutes). The clip length is the render length.
4. `model` picks the engine (`heygen-avatar-6` or the cheaper `heygen-avatar-6-turbo`);
   `model.resolution` picks 1080p or 2k and `model.aspect_ratio` = `auto` keeps the photo's shape.
5. `model.motion_prompt` directs gestures, expression, posture and camera movement (up to 1200
   characters). `model.motion_expressiveness` = `less` damps the gestures.
6. The photo is not used as the first frame: frame one is re-staged from the photo.

### What to expect

- Video of **realistic people in a reference image** is fine; only reference *videos* of realistic
  people are refused (that is the sibling reference-to-video template).
- Output size follows the photo aspect: this 1024x1024 photo comes back 1088x1088.
- `seed` only decides whether the node re-runs; renders are non-deterministic anyway.

</details>

<details><summary>MarkdownNote</summary>

Select and Ctrl-B to enable, then plug the `AUDIO` output to the audio input of the `HeyGen Avatar 6 Reference to Video` node

</details>
