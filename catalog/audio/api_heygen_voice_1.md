# HeyGen Voice 1.0: Voice Clone to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_voice_1)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1-1.webp" width="360" alt="HeyGen Voice 1.0: Voice Clone to Speech api_heygen_voice_1-1.webp">

> Clone a voice from a short recording with HeyGen Voice 1.0, then speak any script in that voice. Connect one audio clip to Instant Clone and the resulting voice_id feeds straight into text to speech, with no training wait. Use the expressiveness control to stay close to the recording or push more emotion into the delivery. Ideal for narration in your own voice, character dialogue, and multilingual voiceover.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_voice_1.json)

## Details

| | |
|---|---|
| Name | `api_heygen_voice_1` |
| Category | Foundation › Audio |
| Output | audio |
| Models | HeyGen |
| Tags | API, Text to Speech, Voice Cloning |
| Type | API |
| Date | 2026-10-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 21 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #2 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenVoiceCloneTextToSpeechNode` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## HeyGen Voice 1.0

Clone a voice from one recording and read any script in it, in a single node: the audio goes in, the speech comes out.

### How to use

1. Sign in with your ComfyUI account before queueing: this node runs on Comfy's servers and bills per use.
2. Record or load **one speaker**, at least 10 seconds of clear speech. Only the first 3 minutes are used, and `remove_background_noise` strips background noise.
3. Write the script in `text` (up to 5000 characters; about 12 minutes of speech, so split very long Chinese or Japanese text).
4. `language` is the language of the text. Set it when auto-detection can confuse closely related languages such as Serbian or Malay.
5. `recording_language` is the language spoken in the recording, `auto` by default.
6. `similarity` controls how closely the voice follows the recording: `medium`, `high`, `extra_high` or `max`. Change `seed` to clone again and get a slightly different voice.
7. `expressiveness_boost` 0.0 stays close to the original recording, 1.0 adds more emotion. 0.5 is the balanced default.
8. Queue the prompt; SaveAudioAdvanced writes the audio.

### Writing the script

- **Plain prose**, 1 to 5000 characters. Anything else is rejected.
- Instant voices ignore `speed` and `pitch`; `expressiveness_boost` (0.0-1.0) is the only delivery control, and `seed` only decides whether the node re-runs.

### Notes

- `heygen-voice-1-turbo` in the model list is faster than `heygen-voice-1`.
- Official docs: [HeyGen Voice](https://developers.heygen.com/docs/models/heygen-voice) and [Text to Speech](https://developers.heygen.com/docs/voices/speech).

</details>
