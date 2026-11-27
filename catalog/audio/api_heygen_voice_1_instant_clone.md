# HeyGen Voice 1.0: Instant Clone TTS

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_voice_1_instant_clone)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1_instant_clone-1.webp" width="360" alt="HeyGen Voice 1.0: Instant Clone TTS api_heygen_voice_1_instant_clone-1.webp">

> Clone a voice from one recording and read any script in it, in a single node: the request clones, speaks and deletes the clone, so nothing is left behind and no HeyGen setup is needed. Ship the reference recording or record a line in the browser; the same inputs cover the quality engine and the ~4x cheaper Turbo engine.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1_instant_clone.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_voice_1_instant_clone.json)

## Details

| | |
|---|---|
| Name | `api_heygen_voice_1_instant_clone` |
| Category | Foundation › Audio |
| Output | audio |
| Models | HeyGen Voice 1.0 |
| Tags | API, Text to Speech, Voice Cloning |
| Type | API |
| Date | 2026-11-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 0 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #1 | audio | casual_voice_reference.wav |
| output | `SaveAudioAdvanced` #3 | audio | api_heygen_voice_1_instant_clone.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenVoiceCloneTextToSpeechNode` | 1 |  |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `RecordAudio` | 1 |  |
| `SaveAudioAdvanced` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## HeyGen Voice 1.0 Instant Clone Text to Speech

Clone a voice from one recording and read a script in it, in a single node: the request clones,
speaks and deletes the clone. No voice-lab upload, no separate clone step, no account setup in
HeyGen, and no clone left behind to occupy the voice slots of our shared workspace.

**Input assets (demo):**
- [casual_voice_reference.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/casual_voice_reference.wav)

### How to use

1. Sign in with your ComfyUI account. This is an API node and bills per use.
2. Load a recording of **one** speaker: at least 10 seconds of clear speech. Only the first
   3 minutes are used, and background noise is stripped when `remove_background_noise` is on.
3. Write what the voice should say in `text` (up to 5000 characters, about 12 minutes of
   speech). `language` is the language of the text; set it for closely related languages
   such as Serbian or Malay, where auto-detection can guess wrong.
4. `recording_language` is the language spoken in the recording, also `auto` by default.
5. `expressiveness_boost` runs 0.0 to 1.0. Higher is more animated, lower stays closer to the
   source voice. 0.5 is the balanced default.
6. `similarity` says how hard the clone follows the recording: `medium`, `high`, `extra_high`
   or `max`. `seed` only decides whether the node re-runs; renders are non-deterministic.

### Two engines

`heygen-voice-1` is the quality pass, `heygen-voice-1-turbo` is about 4x cheaper per thousand
characters. The inputs are identical, so switching engines only changes price and speed.

### Recording your own

`Record Audio` sits below the chain, bypassed: select it and press `Ctrl+B` to enable it, record a line in the browser, then replace the `Load Audio` link with its AUDIO output when you do not want to ship a file.

</details>
