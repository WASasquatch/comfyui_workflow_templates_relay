# Chatter Box: Voice Cloning with TTS

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio-chatterbox_tts)

[▶ audio-chatterbox_tts-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts-1.mp3)

> Upload a short voice clip and input text to generate new speech in the cloned voice.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio-chatterbox_tts.json)

## Details

| | |
|---|---|
| Name | `audio-chatterbox_tts` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Chatter Box |
| Tags | Audio, Voice Cloning |
| Type | open source |
| Date | 2026-01-22 |
| Author | PurzBeats |
| Min ComfyUI version | 0.25.0 |
| Usage | 96 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #6 | audio | chatterbox_input_target_voice.mp3 |

## Custom nodes required

- [comfyui_fill-chatterbox](https://registry.comfy.org/nodes/comfyui_fill-chatterbox)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FL_ChatterboxTTS` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>🎙️ Chatterbox Text-To-Speech</summary>

Clone a voice from a short audio clip and generate new speech using a simple text prompt.

---

## Quick Start

**Input:** short voice clip  
**Output:** generated speech in the same voice

---

## Steps

### 1. Load a Voice
- Add an audio file to the **Load Audio** node  
- Even a **5–10 second** clip is enough  
- This clip is used as the voice reference

### 2. Enter Text
- Type what you want spoken in the **FL Chatterbox TTS** node  
- Write it as you’d naturally say it—pauses and punctuation matter

### 3. (Optional) Tweak Controls
- **Exaggeration** — increases expressiveness  
- **CFG Weight** — how tightly the voice follows the prompt  
- **Temperature** — adds variation and naturalness  
_Default settings work well for first runs_

### 4. Generate
- Click **Run**  
- The generated audio will appear in **Save Audio (Advanced)** (FLAC)

---

## Notes
- Clean, single-speaker recordings give the best results  
- Background noise can affect voice accuracy  
- Try small text changes to hear different inflections

---

</details>
