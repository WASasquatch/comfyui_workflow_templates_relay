# Fish Audio Drama 3: Two-Speaker Dialogue

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_fishaudio_drama3_dialogue)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_dialogue-1.webp" width="360" alt="Fish Audio Drama 3: Two-Speaker Dialogue api_fishaudio_drama3_dialogue-1.webp">

> Generate a multi-speaker scene in one pass with Fish Audio Drama 3: connect one Voice Selector per speaker, mark speaker changes with @Voice1 / @Voice2, and direct the delivery with plain-language [directions] and <whisper> word tags.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_dialogue.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_fishaudio_drama3_dialogue.json)

## Details

| | |
|---|---|
| Name | `api_fishaudio_drama3_dialogue` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Fish Audio |
| Tags | API, TTS |
| Type | API |
| Date | 2026-10-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.40.0 |
| Usage | 26 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #11 | audio | fish_audio_example.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FishAudioVoiceSelector` | 2 |  |
| `FishAudioInstantVoiceClone` | 1 |  |
| `FishAudioTextToSpeech` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Guide</summary>

## Fish Audio Drama 3 — Two-Speaker Dialogue

Generate a whole multi-speaker scene in one pass: every speaker keeps its own voice.

### How to use

1. Sign in with your ComfyUI account. API nodes are pay per use.
2. Write the scene in the `text` field of the Fish Audio Text to Speech node.
3. Mark every speaker change with `@Voice1`, `@Voice2`, and so on: the tags are replaced in order by the voices you connect (up to 5).
4. Connect one Fish Audio Voice Selector per speaker. This template ships with two of the new voices, Delia and Sheila — pick any preset, or set the selector to `custom` and paste a voice ID from fish.audio.
5. Direct the performance with plain-language tags in square brackets, in any language, and change them mid-line.
6. Wrap words that need a different delivery: `<whisper>do not open that door.</whisper>`. Inline sounds such as `[laugh]`, `[sigh]` and `[pause]` work too.
7. Keep the other parameters at their defaults, then queue the prompt and preview the audio.

### Model

- `drama-3` (this template): multi-speaker scenes, `[plain-language directions]` and word tags, 80+ languages.
- `s2.1-pro`: the previous generation, same voice list, emotion cues such as `[happy]` or `[whispering]` at the start of a sentence.
- `s1`: a single voice; emotion cues in parentheses, such as `(happy)`.

Text length and model both change the price: the badge on the node shows the estimate for the current text.

### Cloning your own voice

To use your own voice instead of a preset, select the two nodes in the `Option 2` group and press **Ctrl‑B** to enable them, then point `Load Audio` at a 10–30 second, clean recording of one speaker. The clone becomes the next voice in the list, so add `@Voice3` where it should speak (a two-voice clone setup uses `@Voice1`/`@Voice2`).

</details>
