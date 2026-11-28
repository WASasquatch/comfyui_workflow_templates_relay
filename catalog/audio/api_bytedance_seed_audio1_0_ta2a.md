# Seed Audio 1.0: Text + Audio to Audio

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_seed_audio1_0_ta2a)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ta2a-1.webp" width="360" alt="Seed Audio 1.0: Text + Audio to Audio api_bytedance_seed_audio1_0_ta2a-1.webp">

> Upload a reference audio clip and write a text prompt to clone the voice into a new scene. Generate dialogue, background music, and sound effects with up to 3 reference voices.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ta2a.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seed_audio1_0_ta2a.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seed_audio1_0_ta2a` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Seed Audio 1.0 |
| Tags | API, Audio, Audio Editing |
| Type | API |
| Date | 2026-07-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.27.1 |
| Usage | 85 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #8 | audio | seed_audio_ref_audio1.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedAudio` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: TA2A Prompt Guide</summary>

Seed Audio 1.0: TA2A (Text + Audio to Audio) Workflow Guide

## What This Workflow Does
Load Audio → ByteDance Seed Audio 1.0 (audio reference) → Save Audio.

TA2A = text prompt + reference audio. Clone voice(s) from up to 3 reference clips, then generate a new scene with those voices plus ambience, music, and SFX.

Best for: keeping a consistent character voice, multi-speaker scenes with known voices, dubbing when you already have a voice sample.

## How to Use
1. Load Audio: add your reference clip(s) (≤30s each).
2. Connect AUDIO → reference_audio_1 (and _2, _3 if needed, in order, no gaps).
3. Keep reference_mode on "audio reference".
4. In text_prompt, tag each speaker with voiced by @AudioN matching the connected clip.
5. Run the workflow.

@Audio1 = reference_audio_1 · @Audio2 = reference_audio_2 · @Audio3 = reference_audio_3

Need a reference clip first? Use the T2A workflow to generate a clean single-speaker sample, then use it here.

## Target Language
The model supports English and Chinese. It may mix languages if you do not specify.

To lock the output language, add a bracket tag at the top:
- [Language: English only.]
- [Language: Chinese only.]

Also state the language in each character's voice traits, for example: speaks English only, or speaks Chinese only. Write dialogue in your target language.

## Avoid Scene Text Being Spoken
Wrap non-dialogue in [square brackets]. Only quoted text after says / whispers should be spoken.

## Prompt Guide
1. [Language: ...] optional but recommended
2. [Environment / BGM / SFX: ...]
3. Name (voice traits, voiced by @Audio1) says: "dialogue"
4. Name (voiced by @Audio1), [emotion], says: "next line"
5. Name2 (voice traits, voiced by @Audio2) replies: "dialogue"
6. [Outro]

Rules:
- Every @AudioN in the prompt must have a matching connected clip
- Same speaker reuses the same @AudioN on later lines
- Max 3 reference clips · ≤30s each · connect 1→2→3 without gaps

Limits: prompt ≤3000 chars · output ≤2 min · English & Chinese

## Example (single reference)
[Language: English only.]
[Environment: quiet café ambience, soft room tone, no music.]

Elena (warm mid-range voice, calm and friendly, speaks English only, voiced by @Audio1) says gently:
"Hi, thanks for joining me today."

Elena (voiced by @Audio1), a little warmer, says:
"I'll speak naturally, just like my reference voice."

[Silence.]

</details>
