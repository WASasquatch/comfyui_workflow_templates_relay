# Eleven v4: Text to Dialogue

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_v4_text_to_dialogue-1.webp" width="360" alt="Eleven v4: Text to Dialogue api_elevenlabs_v4_text_to_dialogue-1.webp">

> Generate a multi-speaker dialogue from text with Eleven v4: give every entry its own line and its own voice, direct the delivery with audio tags such as [quietly] or [laughs], or clone a voice from a sample and let it take a turn. One audio file is output. Ideal for podcasts, game dialogue, and character conversations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_v4_text_to_dialogue.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_v4_text_to_dialogue.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_v4_text_to_dialogue` |
| Category | Foundation › Audio |
| Media type | image |
| Models | ElevenLabs |
| Tags | Text to Speech, Audio, API |
| Type | API |
| Date | 2026-10-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.0 |
| Usage | 31 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #210 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ElevenLabsVoiceSelector` | 2 | comfy-core |
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsTextToDialogue` | 1 | comfy-core |
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

## How to use this template

- `inputs` sets how many turns the dialogue has, 1 to 10: every entry is one turn with its own line and its own voice, and the turns are generated in order as a single audio file. This template ships 4 turns that alternate between the two voices.
- Connect a voice to every entry. One Voice Selector can feed several entries, so two selectors (Roger and Laura) already drive a conversation of any length: raise `inputs` and alternate A, B, A, B.
- Option 1, preset voice, is the active path. Option 2, voice clone, is bypassed: select the **Load Audio** (or **Record Audio**) and **ElevenLabs Instant Voice Clone** nodes, press Ctrl+B, then replace that entry's Voice Selector link with the clone's voice output. Use 1 to 2 minutes of clean single-speaker audio for a usable clone: it copies the voice, not the words.

## How to write the lines

- Audio tags inside an entry affect only that turn: `[quietly]`, `[laughs]`, `[deadpan]`. Describe the voice quality rather than a sound cue.
- Punctuation does the timing: `...` trails off, a dash cuts a line short. An interruption is a dash at the end of one entry and at the start of the next. SSML break tags are not supported.
- Keep each entry to one breath, and keep all entries together under 2,000 characters per request.

Prompting guide: [ElevenLabs best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4)


## Input Asset

- [long_demo.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/long_demo.mp3)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
