# Chatter Box: Multi-Speaker Conversation with Cloned Voices

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

[▶ audio-chatterbox_tts_dialog-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts_dialog-1.mp3)

> Upload voice samples and enter a multi-speaker dialog script. Generate a conversation audio file with cloned voices for each speaker.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_tts_dialog.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio-chatterbox_tts_dialog.json)

## Details

| | |
|---|---|
| Name | `audio-chatterbox_tts_dialog` |
| Category | Foundation › Audio |
| Media type | audio |
| Models | Chatter Box |
| Tags | Audio, Text to Speech, Voice Cloning |
| Type | open source |
| Date | 2026-01-22 |
| Author | PurzBeats |
| Min ComfyUI version | 0.25.0 |
| Usage | 24 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #2 | audio | chatterbox_input_target_voice.mp3 |
| input | `LoadAudio` #3 | audio | chatterbox_input_gettysburg.wav |

## Custom nodes required

- [comfyui_fill-chatterbox](https://registry.comfy.org/nodes/comfyui_fill-chatterbox)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 2 |  |
| `AudioCrop` | 1 |  |
| `FL_ChatterboxDialogTTS` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioMP3` | 1 |  |

## Notes embedded in the workflow

<details><summary>🎙️ Chatterbox Dialog TTS</summary>

Generate a multi-speaker conversation using cloned voices and a written dialog.

---

## How to Use

1. **Load voice references**  
   Add a short audio clip for each speaker using the **Load Audio** nodes.  
   (5–10 seconds of clean speech per voice is enough.)

2. **(Optional) Trim clips**  
   Use **AudioCrop** to isolate a clean section of each voice.

3. **Write the dialog**  
   Enter your dialog text in the **FL Chatterbox Dialog TTS** node.

4. **Run the workflow**  
   Click **Run** to generate the conversation.

5. **Listen or export**  
   Preview or save the result from **Save Audio (MP3)**.

---

## Notes

- Clean, distinct voice samples work best  
- Short lines sound more natural than long paragraphs  
- Fewer speakers = faster iteration

---

</details>
