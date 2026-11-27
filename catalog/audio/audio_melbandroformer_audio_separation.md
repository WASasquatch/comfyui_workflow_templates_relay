# MelBandRoFormer Audio Separation

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_melbandroformer_audio_separation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_melbandroformer_audio_separation-1.webp" width="360" alt="MelBandRoFormer Audio Separation audio_melbandroformer_audio_separation-1.webp">

> Load an audio file and separate it into vocal and instrumental stems using the MelBandRoFormer model. Outputs two MP3 files for isolated vocals and background music.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_melbandroformer_audio_separation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_melbandroformer_audio_separation.json)

## Details

| | |
|---|---|
| Name | `audio_melbandroformer_audio_separation` |
| Category | Foundation › Audio |
| Output | audio |
| Models | None |
| Tags | Audio, Audio Editing |
| Type | open source |
| Date | 2026-03-30 |
| Author | ComfyUI |
| Download size | 409.6 MB |
| Min ComfyUI version | 0.25.0 |
| Usage | 23 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #1 | audio | melbandroformer_input.mp3 |

## Custom nodes required

- [ComfyUI-MelBandRoFormer](https://registry.comfy.org/nodes/ComfyUI-MelBandRoFormer)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveAudioAdvanced` | 2 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MelBandRoFormerModelLoader` | 1 |  |
| `MelBandRoFormerSampler` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# MelBandRoFormer Audio Separation

Separates any audio track into vocals and instruments using the MelBandRoFormer model.

## Workflow

1. **LoadAudio** — loads your input audio file
2. **MelBandRoFormerModelLoader** — loads `MelBandRoformer_fp16.safetensors` from `models/diffusion_models/`
3. **MelBandRoFormerSampler** — processes audio and outputs two stems: vocals and instruments
4. **SaveAudioMP3** × 2 — saves each stem as a separate MP3
## Requirements

- **Node:** [ComfyUI-MelBandRoFormer](https://github.com/kijai/ComfyUI-MelBandRoFormer) 
- **Model:** [MelBandRoformer_fp16.safetensors](https://huggingface.co/Kijai/MelBandRoFormer_comfy/resolve/main/MelBandRoformer_fp16.safetensors) (435.3 MB) (~456 MB) Put it under `ComfyUI/models/diffusion_models`

> Input audio should be stereo for best results.

</details>
