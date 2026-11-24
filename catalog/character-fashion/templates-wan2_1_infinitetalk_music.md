# Audio-Driven Character Lip Sync Video

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-wan2_1_infinitetalk_music-1.webp" width="360" alt="Audio-Driven Character Lip Sync Video templates-wan2_1_infinitetalk_music-1.webp">

> Upload a character image and an audio file. Generate a lip-sync video where the character's mouth movements match the provided audio track.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-wan2_1_infinitetalk_music.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-wan2_1_infinitetalk_music.json)

## Details

| | |
|---|---|
| Name | `templates-wan2_1_infinitetalk_music` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Wan2.1 InfiniteTalk |
| Tags | Audio to Video, Lip Sync, Video |
| Type | open source |
| Date | 2026-02-19 |
| Author | hellorob |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.11.0 |
| Usage | 433 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #125 | audio | wan2_1_infinitetalk_audio.mp3 |
| input | `LoadImage` #284 | image | wan2_1_infinitetalk_first_frame.png |
| output | `SaveVideo` #325 | video | templates-wan2_1_infinitetalk_music.mp4 |

## Custom nodes required

- [audio-separation-nodes-comfyui](https://registry.comfy.org/nodes/audio-separation-nodes-comfyui)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |

## Subgraphs

- **Audio to Video (Wan2.1 Infinitalk)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `AudioSeparation` | 1 | audio-separation-nodes-comfyui |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `DownloadAndLoadWav2VecModel` | 1 | ComfyUI-WanVideoWrapper |
| `GetImageSizeAndCount` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MultiTalkModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `MultiTalkWav2VecEmbeds` | 1 | ComfyUI-WanVideoWrapper |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `WanVideoClipVisionEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoImageToVideoMultiTalk` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSampler` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncodeCached` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Desired audio length * 25fps = Max Frames

60 seconds = 1500 frames
```

</details>
