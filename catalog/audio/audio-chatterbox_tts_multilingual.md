# Chatter Box: Multilingual Text-to-Speech with Voice Cloning

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

[▶ audio-chatterbox_tts_multilingual-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts_multilingual-1.mp3)

> Upload a short voice sample and input your text prompt. Select a target language to generate spoken audio in multiple languages using the cloned reference voice.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts_multilingual.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio-chatterbox_tts_multilingual.json)

## Details

| | |
|---|---|
| Name | `audio-chatterbox_tts_multilingual` |
| Category | Foundation › Audio |
| Media type | audio |
| Models | Chatter Box |
| Tags | Audio, Text to Audio, Voice Cloning |
| Type | open source |
| Date | 2026-01-22 |
| Author | PurzBeats |
| Min ComfyUI version | 0.25.0 |
| Usage | 65 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #2 | audio | chatterbox_input_target_voice.mp3 |

## Custom nodes required

- [comfyui_fill-chatterbox](https://registry.comfy.org/nodes/comfyui_fill-chatterbox)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FL_ChatterboxMultilingualTTS` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioMP3` | 1 |  |

## Notes embedded in the workflow

<details><summary>🌍 Chatterbox Multilingual TTS</summary>

Generate spoken audio in multiple languages using a voice reference and a text prompt.

---

## How to Use

1. **Load a voice sample**  
   Upload a short audio clip into the **Load Audio** node.  
   This audio defines the voice that will be used for generation.

2. **Write your prompt**  
   Enter the text you want spoken in the **FL Chatterbox Multilingual TTS** node.

3. **Select the language**  
   Choose the target language from the **language** dropdown.

4. **Run the workflow**  
   Click **Run** to generate the audio.

5. **Listen or export**  
   Preview or save the result from **Save Audio (MP3)**.

---

## Notes

- Short, clean voice samples work best  
- The same voice can be used across multiple languages  
- Default settings are a good starting point

---

</details>
