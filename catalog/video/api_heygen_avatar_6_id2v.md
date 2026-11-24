# HeyGen Avatar 6: Identity to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_6_id2v-1.webp" width="360" alt="HeyGen Avatar 6: Identity to Video api_heygen_avatar_6_id2v-1.webp">

> Write a line and pick a presenter. HeyGen Avatar 6 renders a stock avatar or your own digital twin speaking that script in the chosen voice, with a motion prompt directing gestures, expression, posture and camera. No photo or audio file needed: the node synthesizes the speech, and the frame comes from the look at 1080p or 2K in 16:9, 9:16, 1:1, 4:5, 5:4 or the look's own shape. Avatar 6 or the cheaper Avatar 6 Turbo. Ideal for presenter and explainer clips, product updates and any talking-head shot you would otherwise have to film.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_6_id2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_avatar_6_id2v.json)

## Details

| | |
|---|---|
| Name | `api_heygen_avatar_6_id2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | HeyGen Avatar 6 |
| Tags | API, Lip Sync, Text to Video |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.0 |
| Usage | 0 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | pink_hair_portrait.png |
| input | `LoadAudio` #13 | audio | avatar6_voice_sample.mp3 |
| output | `SaveVideo` #2 | video | api_heygen_avatar_6_id2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `SaveText` | 2 |  |
| `StringConcatenate` | 2 |  |
| `HeyGenAvatar6IdentityToVideoNode` | 1 |  |
| `HeyGenCreateAvatarNode` | 1 |  |
| `HeyGenVoiceCloneNode` | 1 |  |
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## HeyGen Avatar 6: Identity to Video

A talking presenter from a stock look — no photo, no audio file. Pick one of the Avatar 6 looks,
write what they should say, and the node voices it and performs it.

## Input Assets

The default run needs no files. The two optional flows above use:

- [pink_hair_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pink_hair_portrait.png) - photo for `Create your own avatar`
- [avatar6_voice_sample.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/avatar6_voice_sample.mp3) - 17.8 s single-speaker speech for `Create your own voice`

### How to use

1. Sign in with your ComfyUI account. This is an API node, it bills per render.
2. `model` picks the engine: `heygen-avatar-6` (default, higher quality) or `heygen-avatar-6-turbo`
   (cheaper, faster). Switching the engine reveals the same inputs.
3. `avatar` picks a stock look. `custom_avatar_id` overrides it with a look you made in
   HeyGen Create Avatar that supports Avatar 6.
4. `speech` has two modes. **script** writes the line into `text`, picks a `voice` and an optional
   `voice_speed`; **audio** takes your own AUDIO clip instead, and the clip length becomes the
   render length.
5. `resolution` (1080p or 2k) and `aspect_ratio` set the frame: at 1080p, 16:9 renders 1920x1080,
   `auto` follows the look's source footage.
6. `motion_prompt` directs gestures, expression, posture and camera movement (up to 1200
   characters). `motion_expressiveness` = `less` damps the gestures.
7. `seed` only decides whether the node re-runs; renders are non-deterministic anyway.

### What to expect

- The script length is the clip length: this one-sentence script is a 4.5 s read.
- One look + one script renders a single clip. Re-run with a new seed for a different take.

</details>

<details><summary>Note: voice_id and avatar_id</summary>

## Reuse your own avatar and voice

The two groups above are parked, bypassed, so the default prompt stays one cheap render.
Select a group and press **Ctrl+B** to enable it.

### Where the two IDs come from

**Avatar ID** (`avatar_id`)
1. Enable `Create your own avatar for reuse` and load a photo into `Load Image`: head and
   shoulders, face clearly visible, hands out of frame. `pink_hair_portrait.png` ships with
   this template.
2. `HeyGen Create Avatar` with `source = photo` returns the new look's ID on its `avatar_id`
   STRING output, plus a preview frame.
3. `Concatenate Text` prefixes the name you type with the ID and `Save Text` writes it to
   `output/HeyGen_Avatar_*.txt`. Keep that string: it is the ID.

**Voice ID** (`voice_id`)
1. Enable `Create your own voice for reuse` and load at least 10 seconds of one speaker,
   clean and continuous, into `Load Audio`. `avatar6_voice_sample.mp3` ships with this
   template (17.8 s, single speaker).
2. `HeyGen Voice 1.0 Instant Clone` returns the cloned `voice_id` STRING; `Concatenate Text`
   and `Save Text` save it the same way.

### How to use them

- **Avatar**: on `HeyGen Avatar 6 Identity to Video` set `avatar` to `custom avatar`, then
  paste the saved ID into the `custom_avatar_id` field that appears underneath.
- **Voice**: keep `speech` = `script` and paste the saved ID into the optional
  `custom_voice_id` field. It wins over the `voice` dropdown whenever it is non-empty, so
  leave it empty to fall back to a stock voice.
- Or route the cloned voice through `HeyGen Voice 1.0 Text to Speech` (`voice_id` + `text`)
  and switch `speech` to `audio` with that AUDIO plugged in.
- Both IDs are scoped to the HeyGen workspace behind the Comfy account you are signed in
  with: an ID made in one workspace will not resolve in another.

</details>
