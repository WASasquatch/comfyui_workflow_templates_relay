# Eleven v4: Text to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_elevenlabs_v4_text_to_speech)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_v4_text_to_speech-1.webp" width="360" alt="Eleven v4: Text to Speech api_elevenlabs_v4_text_to_speech-1.webp">

> Generate expressive speech from text with Eleven v4, the quality-focused ElevenLabs model. Direct the performance with audio tags such as [whispers] or [excited] written into the script, or upload a voice sample to clone a voice and narrate the script in it. One audio file is output. Ideal for audiobooks, narration, and character voiceovers.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_v4_text_to_speech.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_v4_text_to_speech.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_v4_text_to_speech` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ElevenLabs |
| Tags | Text to Speech, Audio, API |
| Type | API |
| Date | 2026-10-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.0 |
| Usage | 518 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #210 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsTextToSpeech` | 1 | comfy-core |
| `ElevenLabsVoiceSelector` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `RecordAudio` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>How to enable bypassed nodes</summary>

```text
Please select and use Ctrl-B to enable the bypassed nodes.
```

</details>

<details><summary>MarkdownNote</summary>

## How to write the prompt

Eleven v4 and v4 Turbo treat the prompt as a performance script. Audio tags in square brackets set the delivery: `[whispers]`, `[laughs]`, `[sighs]`, `[excited]`, `[sarcastic]`, `[crying]` are a starting point. Place a tag right before or after the words it should affect.

- Describe the voice quality instead of a sound cue: `[low, gravelly voice]` is clearer than a vague tag, because v4 can read an ambiguous tag as a request for a sound effect.
- Punctuation sets the pacing: ellipses add pauses, capitals add emphasis, standard punctuation keeps a natural rhythm. SSML break tags are not supported, and v4 has no speed or style slider.
- Match the tags to the voice: a calm narration voice follows `[whispers]` more reliably than `[giggles]`. Combine tags such as `[annoyed] [under your breath]` for a more complex delivery.
- Stability controls how consistent the delivery stays: lower values are more expressive, higher values more monotone. Similarity controls how closely the output follows the reference voice.
- `apply_text_normalization` covers numbers, dates and abbreviations. Keep the text within the model's limit: 10,000 characters per request for Eleven v4.

Example prompt:

```text
[whispers] I never knew it could be this way, but I'm glad we're here.
```

The **ElevenLabs Text to Speech** node ships with a demo script that uses these techniques: run it once to hear how the tags land, then replace the text with your own script.

More techniques: [ElevenLabs prompting guide](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4)


## Input Asset

- [long_demo.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/long_demo.mp3)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
