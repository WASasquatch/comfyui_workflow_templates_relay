# MiniMax Music 3: Text to Music

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_minimax_music_3)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_minimax_music_3-1.webp" width="360" alt="MiniMax Music 3: Text to Music audio_minimax_music_3-1.webp">

> Create full-length songs from text prompts with MiniMax Music 3, generating complete 5-minute tracks with stable structure and high-fidelity audio. Input a structured caption describing lyrics, style, mood, and arrangement, and receive a finished song as output. Ideal for music producers prototyping demos, and content creators needing original background tracks.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_minimax_music_3.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_minimax_music_3.json)

## Details

| | |
|---|---|
| Name | `audio_minimax_music_3` |
| Category | Foundation › Audio |
| Output | audio |
| Models | MiniMax Music 3 |
| Tags | Audio, Text to Music |
| Type | open source |
| Date | 2026-08-13 |
| Author | ComfyUI |
| Download size | 14.3 GB |
| Min ComfyUI version | 0.33.1 |
| Usage | 403 |
| Nodes | 14 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_music3_dit_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/diffusion_models/minimax_music3_dit_fp16.safetensors) |
| `minimax_music3_text_encoder_pruned_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors) |
| `minimax_music3_dav.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/vae/minimax_music3_dav.safetensors) |

## Subgraphs

- **Text to Music (MiniMax Music 3)** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyMiniMaxMusic3LatentAudio` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MiniMaxMusic3TextEncode` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 | comfy-core |
| `SeedNode` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `VAEDecodeAudioTiled` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: MiniMax Music 3</summary>

## MiniMax Music 3

A music generation model by MiniMax that creates complete songs up to 5 minutes long with stable structure and high audio quality. Two inputs drive it: **Caption** (structured music description: style, mood, vocals, arrangement) and **Lyrics** (with `[intro]` `[verse]` `[chorus]` `[bridge]` `[outro]` tags controlling song structure).

### Parameters

| Parameter | Description |
|---|---|
| Caption | Music description. Write it in three sections — Global Metadata → Vocal Details → Arrangement. The more specific, the closer the result. |
| Lyrics | Song lyrics + section tags. Tags are the only executable structural instructions; the lyric text itself only conveys mood. |
| max_duration | Target song length in seconds (default 120 = 2 minutes; the model supports up to ~300 s / 5 minutes). Longer songs take more time and VRAM. |
| seed | Random seed for the generation. Keep it fixed to reproduce the same song; change it to get a different take. |
| Model files | diffusion model / text encoder / VAE.|
| Tiled decode | Decode the audio VAE in overlapping tiles to drastically cut VRAM usage — helpful for long songs on low-VRAM GPUs. Slightly slower, with a small risk of seams at tile boundaries; turn it off on high-VRAM GPUs for the best quality. |

### Prompt Writing Guide

You can find an official [Music Caption Rewriter Skill here](https://github.com/MiniMax-AI/MiniMax-Music3)

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-Music-3](https://huggingface.co/Comfy-Org/MiniMax-Music-3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-Music-3](https://modelscope.cn/models/Comfy-Org/MiniMax-Music-3)

**diffusion_models**
- [minimax_music3_dit_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/diffusion_models/minimax_music3_dit_int8_convrot.safetensors) (2.33 GB) # For low VRAM
- [minimax_music3_dit_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/diffusion_models/minimax_music3_dit_fp16.safetensors) (4.58 GB)

**text_encoders**

- [minimax_music3_text_encoder_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors) (8.57 GB)

**vae**

- [minimax_music3_dav.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/vae/minimax_music3_dav.safetensors) (206.7 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── minimax_music3_dit_int8_convrot.safetensors # For low VRAM
│   │   └── minimax_music3_dit_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └── minimax_music3_text_encoder_pruned_int8_convrot.safetensors
│   └── 📂 vae/
│       └── minimax_music3_dav.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
