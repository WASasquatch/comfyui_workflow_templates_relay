# Seed Audio 1.0: Text + Image to Audio

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ti2a-1.webp" width="360" alt="Seed Audio 1.0: Text + Image to Audio api_bytedance_seed_audio1_0_ti2a-1.webp">

> Upload a character image and write a text prompt to generate audio. The model derives the voice from your image, then produces speech, ambience, background music, and sound effects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ti2a.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seed_audio1_0_ti2a.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seed_audio1_0_ti2a` |
| Category | Foundation › Audio |
| Media type | image |
| Models | Seed Audio 1.0 |
| Tags | API, Text to Audio |
| Type | API |
| Date | 2026-07-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.27.1 |
| Usage | 16 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | girl_and_fish.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: TI2A Prompt Guide</summary>

Seed Audio 1.0: TI2A (Text + Image to Audio) Workflow Guide

## What This Workflow Does
Load Image → ByteDance Seed Audio 1.0 (image reference) → Save Audio.

TI2A = text prompt + reference image. The model derives the character voice from your image, then generates speech, ambience, music, and SFX from your prompt.

Best for: character art, portraits, or scene images when you have no reference audio. One image = one derived voice.

## How to Use
1. Load Image: upload a clear character image (portrait or upper body works best).
2. Connect IMAGE → Seed Audio reference_image input.
3. Keep reference_mode on "image reference".
4. Write text_prompt matching your scene (see format below).
5. Run the workflow.

Do NOT use @Audio1 / @Audio2 / @Audio3 in this mode.

## Target Language
The model supports English and Chinese. It may mix languages if you do not specify.

To lock the output language, add a bracket tag near the top of your prompt:
- [Language: English only.]
- [Language: Chinese only.]

Also state the language in the character's voice traits, for example: speaks English only, or speaks Chinese only. Write all dialogue in your target language.

Image reference controls voice tone and character feel. Language is controlled by your prompt.

## Avoid Scene Text Being Spoken
Plain prose at the start may be read aloud as narration, making the audio too long.

Wrap anything that is NOT dialogue in [square brackets]:
- [Environment: ...] for location, weather, ambience
- [Background music: ...] for BGM style and mood
- [Language: English only.] or [Language: Chinese only.] for output language
- [Long pause. ...] for effects and stage directions
- [Outro: ...] for ending

Only text in quotes after says / whispers should be spoken. Keep dialogue short.

## Prompt Guide
1. [Language: ...] recommended
2. [Environment: ...]
3. [Background music / SFX: ...]
4. Character (delivery traits, target language) says / whispers: "dialogue only"
5. [Beat / pause / SFX]
6. [Outro]

Limits: prompt ≤3000 chars · output ≤2 min · English & Chinese

## Example
[Language: English only.]
[Environment: quiet dreamlike garden at dusk, soft blue light, petals drifting, faint water ripples.]
[Background music: gentle piano and airy strings, melancholic and ethereal.]

The girl (young woman, soft breathy voice, quiet and fragile, dreamy, slightly sad, speaks English only) whispers:
"I thought the flowers would stay with me forever."

[Long pause. Petals fall. Water shimmers.]

She (same voice, a little warmer) says softly:
"Maybe that is why this place feels beautiful."

[Background music fades to silence.]

</details>
