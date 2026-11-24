# Breeze TTS 2: Text to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/breeze_tts2_tts-1.webp" width="360" alt="Breeze TTS 2: Text to Speech breeze_tts2_tts-1.webp">

> Turn a script into speech with Breeze TTS 2, Breeze Blue's open-weight voice model: native English and Chinese, plus a 51-language multilingual mode. Clone a voice from a three-second recording, design a new one from a written description, or start from a featured voice, then direct the performance in plain language or with inline audio tags such as (sighs). The workflow ships a sample recording, a saved voice id you can reuse, and optional Remix and Design tools. Ideal for narration, character dialogue and localized voiceover.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/breeze_tts2_tts.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/breeze_tts2_tts.json)

## Details

| | |
|---|---|
| Name | `breeze_tts2_tts` |
| Category | Foundation › Audio |
| Media type | image |
| Models | Breeze Blue |
| Tags | API, TTS, Voice Cloning |
| Type | API |
| Date | 2026-11-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.4 |
| Usage | 0 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #9 | audio | breeze_tts2_tts_clone_audio.wav |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 5 |  |
| `BreezeVoiceSelector` | 2 |  |
| `BreezeTextToSpeech` | 1 |  |
| `BreezeVoiceClone` | 1 |  |
| `BreezeVoiceDesign` | 1 |  |
| `BreezeVoiceRemix` | 1 |  |
| `LoadAudio` | 1 |  |
| `PreviewAny` | 1 |  |
| `RecordAudio` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `SaveText` | 1 |  |
| `StringConcatenate` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: clone → saved voice id</summary>

**Voice clone — input to reusable voice id**

`Load Audio → Breeze Voice Clone → Preview as Text`

- One speaker, **at least 3 s**. Only the first **60 s** of the file are read;
  Breeze keeps the best ≤30 s, trims it clean and normalises the loudness.
- `remove_background_noise` helps on a rough phone take.
- `voice` output = the new **voice id** (`voc_…`), shown by *Preview as Text*.
  `preview` output = how it sounds.
- Only clone a voice you have the right to use — consent is required.

**Reuse the id later:** paste it into *Breeze Voice Selector → custom*.
*Concatenate Text* adds a readable prefix and *Save Text* writes the id to a
`.txt` for your records.

Sample to try: [breeze_tts2_tts_clone_audio.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/breeze_tts2_tts_clone_audio.wav).

</details>

<details><summary>Note: Voice Remix</summary>

## Breeze Voice Remix

Makes a **changed copy** of a voice you already have, in that voice's language.

- `change = custom` — describe the shift in words: "older, huskier, tired, a
  little slower".
- `change = preset` — 27 named shifts:
  **age** (teenage → elderly) · **gender** (male imitating female, and reverse) ·
  **pitch** (higher / lower) · **pace** (faster / slower) ·
  **energy** (energetic / low-energy) ·
  **emotion** (excited, angry, sad, afraid, awkward, sarcastic, restrained
  grief, painful) ·
  **role-play** (stage actor, news anchor, bedtime storyteller) ·
  **delivery** (laughing, crying, whispered, singing).
- `strength` 1–10 — how far it moves from the original. 4 is a good start.

Outputs: a new **voice id** (saved to your account) and an audio **preview**.
Send the voice to *Breeze Text to Speech*, or save the id for later runs.

Need another language? Use *Breeze Voice Localize* — Remix stays in the same
language.

</details>

<details><summary>Note: Voice Design</summary>

## Breeze Voice Design

Invents a **new voice from words** — no reference audio needed.

- `description` (3–500 chars) — who the voice is: age, gender, accent, timbre,
  pace, character. e.g. "Warm male voice in his mid-forties with a soft Scottish
  accent, close-miked, unhurried, with dry humour underneath."
- `preview_text` (≤500 chars) — the line the new voice speaks. **The voice is
  built from this line**, so write it in the target language and in the tone you
  want; audio tags such as `(sighs)` work here too.
- `language` + `model` — same rule as text to speech: English and Chinese can use
  either model, every other language uses the multilingual one.
- `strength` 1–10 — how literally it follows the description.
- Reroll `seed` for another take on the same description.

Outputs: the **voice id** (named after the description, saved to your account)
and an audio **preview**. Send the voice to *Breeze Text to Speech*.

</details>

<details><summary>Note: Breeze TTS 2 — read me first</summary>

# Breeze TTS 2 — voice toolkit

**Breeze TTS 2** (by Breeze Blue) is an open-weight text-to-speech model built for
real-time speech. One model speaks **English and Chinese** natively and a
multilingual variant covers **51 languages**. Delivery is steerable with plain
words, and a voice can be cloned from a 3-second sample or designed from a
written description.

These are **partner nodes**: they run on Comfy's servers, so sign in to Comfy and
keep API credits available.

| Model | Languages |
| --- | --- |
| Breeze TTS 2 | English, Chinese |
| Breeze TTS 2 Multilingual | all 51 (only option outside English/Chinese) |

## What this workflow does

**Step 1 — create a voice**
`Load Audio → Breeze Voice Clone → Preview as Text`
The clone node returns a **voice id** (`voc_…`) plus a spoken preview. The id is
shown in *Preview as Text*, gets a readable prefix, and *Save Text* writes it to
a `.txt` so you can reuse it in later runs.

**Step 2 — speak the script**
`Breeze Voice Selector (custom) → Breeze Text to Speech → Save Audio`
The selector passes the cloned id into *Breeze Text to Speech*. Output lands in
`ComfyUI/output/audio/Breeze_TTS2…`.

**Optional — a featured voice** (group on the right)
*Breeze Voice Selector* set to `English → Elizabeth` is a ready-made voice: bypass
the clone branch and wire it where the custom selector sits.

**Voice tools** (bottom group — select all, then **Ctrl+B** to enable)
*Breeze Voice Remix* reshapes a voice you already have; *Breeze Voice Design*
invents a new one from words. Each returns a voice id + preview; connect either
to *Breeze Text to Speech*.

## Writing the script

- 1–1000 characters per request.
- Audio tags are **performed, not read**: `(sighs)`, `(laughs)`, `(whispers)` in
  English — `[叹气]`, `[笑]`, `[咳嗽]` in Chinese.
- `delivery = neutral` keeps the voice as it is; `speaker_boost` pulls it closer
  to the original sound. `delivery = directed` follows `instructions` written in
  the text's language, and `strength` (1–10) sets how hard it leans on them.
- `speed` 0.5–2.0 changes tempo, never pitch.
- A voice sounds best in its own language. For another language, make a native
  copy with *Breeze Voice Localize* instead of feeding foreign text to the voice.

## Input asset

- [breeze_tts2_tts_clone_audio.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/breeze_tts2_tts_clone_audio.wav) — the sample recording wired into `Load Audio`. Download it into `ComfyUI/input/`, or swap `Load Audio` for **Record Audio** and capture a take straight from the mic.
- Any clean single-speaker clip of 3 s or more works.

</details>

<details><summary>MarkdownNote</summary>

Currently ComfyUI doesn't have remote resource preview capability, so you can preview the built-in audio :(

</details>
