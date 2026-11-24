# Fish Audio Drama 3: Directed Performance

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_fishaudio_drama3_directed)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_directed-1.webp" width="360" alt="Fish Audio Drama 3: Directed Performance api_fishaudio_drama3_directed-1.webp">

> Direct a single Fish Audio Drama 3 performance from the text: shift the delivery mid-line with [plain-language directions] and wrap words with <whisper>...</whisper> tags.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_directed.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_fishaudio_drama3_directed.json)

## Details

| | |
|---|---|
| Name | `api_fishaudio_drama3_directed` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Fish Audio |
| Tags | API, TTS |
| Type | API |
| Date | 2026-10-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.40.0 |
| Usage | 91 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #11 | audio | fish_audio_example.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FishAudioInstantVoiceClone` | 1 |  |
| `FishAudioTextToSpeech` | 1 |  |
| `FishAudioVoiceSelector` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Guide</summary>

## Fish Audio Drama 3 — Directed Performance

One voice, acted out with directions and word-level tags.

### How to use

1. Sign in with your ComfyUI account. API nodes are pay per use.
2. Write the script in the `text` field of the Fish Audio Text to Speech node.
3. Add `[directions]` in square brackets wherever the delivery should shift. A direction applies until the next one, so place it exactly where you want the change.
4. Wrap individual words for a different delivery: `<whisper>It is all in the timing.</whisper>`. Inline sounds such as `[laugh]`, `[sigh]` and `[pause]` work in the same way.
5. Pick a voice in the Fish Audio Voice Selector — Delia is connected by default. Set it to `custom` to paste a voice ID from fish.audio.
6. Keep the other parameters at their defaults, then queue the prompt and preview the audio.

### Model

- `drama-3` (this template): `[plain-language directions]` and word tags, 80+ languages, and multi-speaker dialogue via `@Voice1`, `@Voice2`.
- `s2.1-pro`: the previous generation; emotion cues such as `[happy]` at the start of a sentence.
- `s1`: a single voice; emotion cues in parentheses, such as `(happy)`.

Text length and model both change the price: the badge on the node shows the estimate for the current text.

### Cloning your own voice

To read the script in your own voice, select the two nodes in the `Option 2` group and press **Ctrl‑B** to enable them, then point `Load Audio` at a 10–30 second, clean recording. With two voices connected, mark the text with `@Voice1` and `@Voice2`.

</details>
