# Creatify Aurora 2.0: Talking Avatar

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_creatify_aurora_2_avatar)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_creatify_aurora_2_avatar-1.webp" width="360" alt="Creatify Aurora 2.0: Talking Avatar api_creatify_aurora_2_avatar-1.webp">

> Turn one portrait and one voice track into a talking or singing clip. Aurora 2.0 animates the mouth and upper body from the audio, passes the audio through unchanged, and returns a clip exactly as long as the audio — stage the performance with an optional text prompt instead of a second model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_creatify_aurora_2_avatar.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_creatify_aurora_2_avatar.json)

## Details

| | |
|---|---|
| Name | `api_creatify_aurora_2_avatar` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | Creatify Aurora 2.0 |
| Tags | API, Lip Sync, Video |
| Type | API |
| Date | 2026-11-20 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.2 |
| Usage | 0 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | glitter_girl_portrait.png |
| input | `LoadAudio` #11 | audio | glitter_girl_speech.flac |
| output | `SaveVideo` #4 | video | api_creatify_aurora_2_avatar.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BreezeTextToSpeech` | 1 |  |
| `BreezeVoiceClone` | 1 |  |
| `BreezeVoiceSelector` | 1 |  |
| `CreatifyAurora2AvatarNode` | 1 |  |
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `RecordAudio` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Input Assets</summary>

## Creatify Aurora 2.0 Avatar

**Turn one portrait and one voice track into a talking or singing clip.** Aurora 2.0 animates the mouth and the upper body from the audio, passes the audio through unchanged, and returns a clip exactly as long as the audio — stage the performance with an optional text prompt instead of a second model.

**Input assets (demo):**
- [glitter_girl_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/glitter_girl_portrait.png) — 896 x 1152 front-facing portrait, glitter make-up, mouth visible (required workflow input).
- [glitter_girl_speech.flac](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/glitter_girl_speech.flac) — 10.0 s speech track; the clip is exactly this long (required workflow input).

### What this graph does

1. **Load Image**: the portrait. It needs at least 256 px on each side and an aspect ratio between 1:4 and 4:1; the portrait's aspect ratio also sets the frame shape of the clip.
2. **Audio**: three input paths; the sample track ships connected, so switching to another one is a rewire.
   - **Load Audio** (default): the sample track above, already wired into the avatar node's `audio` input.
   - **Record Audio**: shipped **Bypassed**. Select it, press **Ctrl+B** to enable it and record a line, then replace the avatar's `audio` link with its AUDIO output.
   - **Breeze Text to Speech** group (`Breeze Voice Selector` → `Breeze Text to Speech` → `Save Audio Advanced`): shipped **Bypassed**. Enable the group with **Ctrl+B** to synthesize the typed line; its AUDIO output only feeds `Save Audio Advanced`, so replace the avatar's `audio` link with the `Breeze Text to Speech` AUDIO output to hear it in the clip.
   - **Breeze Voice Clone**: shipped **Bypassed**, with nothing wired into its AUDIO input. Enable it, connect a reference recording you have the rights to use, then replace the `Breeze Voice Selector` → `voice` link with the clone's voice output to speak in the cloned voice.
3. **Creatify Aurora 2.0 Avatar**: animates the performance. `text_prompt` is optional staging direction for scene, camera, lighting, expression and motion.
4. **Save Video**: writes the MP4.

---

### Controls

| Control | What it does |
|---|---|
| `resolution` | `480p`, `720p` (default), `1080p` or `2k`. Billed per started second. |
| `text_prompt` | Optional scene, camera, lighting, expression or motion direction. |
| `seed` | Controls whether the node re-runs; results are non-deterministic regardless of seed. |

---

### Limitations

- Clip length equals audio length: the 10.0 s sample renders a 10.0 s clip. Trim the audio to the length you want; there is no duration widget.
- Audio ceiling is 60 s at 480p, 720p and 1080p, and 14 s at 2k. Longer input is refused.
- Billing is per started second of output at the chosen resolution.
- Renders are non-deterministic: the seed only decides whether the node re-runs, it does not reproduce an earlier clip.
- The node animates the face and the upper body, it does not relight the shot, so start from a portrait that is already lit the way you want it.

---

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare the input assets.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
