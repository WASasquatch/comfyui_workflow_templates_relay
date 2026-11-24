# YuE2: Music Cover

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_music_cover-1.webp" width="360" alt="YuE2: Music Cover audio_yue2_music_cover-1.webp">

> Create a new version of a song from reference audio with YuE2. Preserve the original melody while changing the musical style, vocals, lyrics, and arrangement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_music_cover.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_yue2_music_cover.json)

## Details

| | |
|---|---|
| Name | `audio_yue2_music_cover` |
| Category | Foundation › Audio |
| Media type | image |
| Models | YuE2 |
| Tags | Music Cover, Int8 |
| Type | open source |
| Date | 2026-09-14 |
| Author | ComfyUI |
| Download size | 5.0 GB |
| Min ComfyUI version | 0.36.0 |
| Distributions | local |
| Usage | 22 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #45 | audio | yue2_reference_song.flac |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sheetsage2_bf16.safetensors` | `audio_encoders` | [link](https://huggingface.co/Comfy-Org/YuE2/resolve/main/audio_encoders/sheetsage2_bf16.safetensors) |
| `yue2_3b_int8_convrot.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/YuE2/resolve/main/checkpoints/yue2_3b_int8_convrot.safetensors) |

## Subgraphs

- **Music Cover (YuE2)** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 2 |  |
| `AudioEncoderLoader` | 1 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `ConditioningZeroOut` | 1 |  |
| `EmptyYuE2LatentAudio` | 1 |  |
| `KSampler` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `SeedNode` | 1 |  |
| `SheetSage2AudioToABC` | 1 |  |
| `VAEDecodeAudio` | 1 |  |
| `YuE2GenerateMusic` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# YuE2: Music Cover

Create a new version of an existing song with YuE2.

This workflow uses **SheetSage2** to transcribe the melody from the reference audio into an editable ABC score, then uses YuE2 to regenerate the song with a new **Style** and **Lyrics**.

## Input Asset

- [yue2_reference_song.flac](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/yue2_reference_song.flac)

## Model Links

- [Hugging Face:Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2)
- [ModelScope:Comfy-Org/YuE2](https://modelscope.cn/models/Comfy-Org/YuE2)

**checkpoints**

- [yue2_3b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/YuE2/resolve/main/checkpoints/yue2_3b_int8_convrot.safetensors) (3.69 GB)

**audio_encoders**

- [sheetsage2_bf16.safetensors](https://huggingface.co/Comfy-Org/YuE2/resolve/main/audio_encoders/sheetsage2_bf16.safetensors) (1.29 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── yue2_3b_int8_convrot.safetensors
│   └── 📂 audio_encoders/
│       └── sheetsage2_bf16.safetensors
```

## How to Use

[Subgraph](https://docs.comfy.org/interface/features/subgraph)

1. Load a reference song in **Audio**.
2. Describe the new musical direction in **Style**.
3. Enter the lyrics you want to sing in **Lyrics**.
4. Run the workflow to generate a new cover version.

The reference audio provides the melody, while YuE2 creates a new performance and arrangement based on your Style and Lyrics.

## Writing the Style

Describe the target musical style clearly.

Useful elements include:

- **Genre:** jazz, pop, rock, folk, electronic
- **Vocals:** warm male vocal, expressive female vocal, soft vocals
- **Language:** English, Chinese, Japanese, etc.
- **Tempo:** 90 BPM, slow, upbeat
- **Instruments:** piano, guitar, bass, drums, strings, synths
- **Mood:** intimate, energetic, nostalgic, cinematic

Example:

> English, soulful jazz-pop, expressive male vocal, relaxed 88 BPM, Rhodes piano, upright bass, brushed drums, warm saxophone, intimate late-night atmosphere

## Writing Lyrics

Use section tags such as:

    [Verse]
    Streetlights shimmer on the pavement
    Midnight breathing soft and slow

    [Chorus]
    Stay with me until the morning
    Let the city fade away

You can use:

`[Verse]` · `[Chorus]` · `[Bridge]` · `[Outro]`

For better melody matching, keep the new lyrics reasonably close to the original phrasing and syllable count.

## How the Cover Works

The workflow does not directly use the reference audio as YuE2 conditioning.

Instead:

    Reference Audio
        ↓
    SheetSage2
        ↓
    Melody ABC
        ↓
    YuE2 + Style + Lyrics
        ↓
    New Cover Audio

SheetSage2 converts the source recording into a symbolic melody representation. YuE2 then uses that melody as the musical plan for the new cover.

## Tips

- Keep **Style** focused on the target sound, not the original sound.
- Use **melody-only** planning for most cover tasks.
- Changing the Style can create a very different arrangement while preserving the melody.
- Lyrics can be changed, but similar phrasing and syllable counts usually fit the original melody better.
- For a simple style-transfer test, keep the original lyrics and only change the Style.
- For a stronger reinterpretation, change both the Style and Lyrics.

## Learn More

- [YuE2 Cover Guide](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md)
- [YuE2 Music Skill](https://github.com/multimodal-art-projection/YuE/blob/main/skills/yue2-music/SKILL.md)
- [Generation & Covers Reference](https://github.com/multimodal-art-projection/YuE/blob/main/skills/yue2-music/references/generation-and-covers.md)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
