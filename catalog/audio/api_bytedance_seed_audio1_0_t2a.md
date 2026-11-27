# Seed Audio 1.0: Text to Audio

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_seed_audio1_0_t2a)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_t2a-1.webp" width="360" alt="Seed Audio 1.0: Text to Audio api_bytedance_seed_audio1_0_t2a-1.webp">

> Input a text prompt to generate speech, dialogue, background music, and sound effects in one audio file. Describe voices, emotion, and scene details to create multi-speaker audio up to 2 minutes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_t2a.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seed_audio1_0_t2a.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seed_audio1_0_t2a` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Seed Audio 1.0 |
| Tags | Text to Audio, API, Audio |
| Type | API |
| Date | 2026-07-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.27.1 |
| Usage | 52 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: T2A Prompt Guide</summary>

Seed Audio 1.0: T2A (Text to Audio) Workflow Guide

## What This Workflow Does
ByteDance Seed Audio 1.0 (text only) → Save Audio.

T2A = text prompt only. No reference image or audio. Describe the full scene in one prompt: voices, dialogue, ambience, background music, and sound effects. The model generates them together.

Best for: quick scenes, multi-character dialogue, audiobook clips, dubbing when you can describe each voice in text. Also use this workflow to create a clean reference clip for the TA2A workflow.

## How to Use
1. Open ByteDance Seed Audio 1.0 and keep reference_mode on "text only".
2. Write your scene in text_prompt (see format below).
3. Run the workflow. Output saves via Save Audio.

No extra inputs required. Do NOT use @Audio1 / @Audio2 / @Audio3 in this mode.

## Target Language
The model supports English and Chinese. It may mix languages if you do not specify.

To lock the output language, add a bracket tag at the top:
- [Language: English only.]
- [Language: Chinese only.]

Also state the language in each character's voice traits, for example: speaks English only, or speaks Chinese only.

## Avoid Scene Text Being Spoken
Plain prose without brackets may be read aloud as narration, making the audio too long.

Wrap anything that is NOT dialogue in [square brackets]:
- [Environment: ...] for location, weather, ambience
- [Background music: ...] for BGM style and mood
- [SFX: ...] or [Long pause. ...] for effects and stage directions
- [Outro: ...] for ending

Only text in quotes after says / replies / whispers should be spoken.

## Prompt Guide
1. [Language: ...] optional but recommended
2. [Environment: ...]
3. [Background music / SFX: ...]
4. Character voice (gender, age, accent, emotion, tone, pace, target language)
5. Exact dialogue in quotes
6. [Beats / outro]

Limits: prompt ≤3000 chars · output ≤2 min · English & Chinese

## Example
[Language: English only.]
[Environment: quiet coffee shop on a rainy afternoon, rain on window, soft room tone.]
[Background music: soft jazz from an old speaker.]

Leo (young man, tired but warm voice, American accent, speaks English only) says slowly:
"I didn't think you'd actually show up."

Nina (young woman, soft careful voice, speaks English only) replies gently:
"Neither did I. But here we are."

[Long pause. Spoon stirring a cup. Rain grows louder. Jazz piano swells.]
[Music fades. Rain continues. Silence.]

</details>
