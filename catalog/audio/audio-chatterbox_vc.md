# Chatter Box: Voice Cloning Audio Conversion

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio-chatterbox_vc)

[▶ audio-chatterbox_vc-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_vc-1.mp3)

> Upload an audio clip and a short voice reference to generate a converted audio output that clones the target voice while preserving the original timing and performance.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio-chatterbox_vc.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio-chatterbox_vc.json)

## Details

| | |
|---|---|
| Name | `audio-chatterbox_vc` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Chatter Box |
| Tags | Audio, Audio Editing, Voice Cloning |
| Type | open source |
| Date | 2026-01-22 |
| Author | PurzBeats |
| Min ComfyUI version | 0.25.0 |
| Usage | 23 |
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
| `FL_ChatterboxVC` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>🎙️ Chatterbox Voice Cloning (Audio → Audio)</summary>

This workflow takes one audio clip and converts it into another voice while preserving the original timing and performance.

---

## What This Does

- **Input audio**: the speech or performance you want to convert  
- **Target voice**: a short reference clip of the voice you want to clone  
- **Output**: the original audio re-spoken in the target voice

---

## How to Use

### 1. Load the Source Audio
- Upload the audio you want to convert into the **top Load Audio** node  
- This is the performance that will be re-voiced

### 2. (Optional) Trim the Audio
- Use **AudioCrop** to select a specific section  
- Adjust `start_time` and `end_time` to isolate the part you want
- You can bypass the **AudioCrop** node if you don't need to trim your clip

### 3. Load the Target Voice
- Upload a short reference clip into the **bottom Load Audio** node  
- 5–10 seconds of clean speech works well  
- This audio defines the cloned voice

### 4. Generate the Voice Conversion
- The **FL Chatterbox VC** node takes:
  - `input_audio` → the source performance
  - `target_voice` → the voice reference
- Click **Run** to generate

### 5. Listen or Export
- Preview the result in **Save Audio (MP3)**  
- The output keeps the original timing, phrasing, and cadence

---

## Tips

- Clean, single-speaker reference clips give the best results  
- Shorter, well-cropped segments are more reliable  
- If results sound off, try trimming silence or reducing background noise

---

</details>
