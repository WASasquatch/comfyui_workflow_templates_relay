# Video Extend: Seedance 2.5

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_extend-1.webp" width="360" alt="Video Extend: Seedance 2.5 api_seedance2_5_video_extend-1.webp">

> Extend an existing video forward or backward by generating new segments that seamlessly preserve the original characters, scenes, and aspect ratio. The source video must be 1.9–30 seconds long, and you specify the duration of the new clip (4–30 seconds, default 5), with output delivered as MP4 or MOV. Ideal for continuing unfinished footage, creating extended narrative sequences, and building longer edit chains.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_extend.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_video_extend.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_video_extend` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | Seedance 2.5 |
| Tags | Video Extend |
| Type | API |
| Date | 2026-08-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 68 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #35 | video | sloth_bullfight.mp4 |

## Subgraphs

- **Merge Videos** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 | comfy-core |
| `GetVideoComponents` | 2 | comfy-core |
| `PrimitiveBoolean` | 2 | comfy-core |
| `SaveVideo` | 2 |  |
| `AudioConcat` | 1 |  |
| `BatchImagesNode` | 1 | comfy-core |
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `CreateVideo` | 1 | comfy-core |
| `EmptyAudio` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ResizeAndPadImage` | 1 | comfy-core |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Video Extend</summary>

**Input Assets** 
- [sloth_bullfight.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sloth_bullfight.mp4)

This template extends an existing video forward or backward for a new segment (default 5 seconds). The model keeps the character, scene, aspect ratio, and overall style consistent with your source footage. Only the new segment is generated; the source video is not included in the output.

**How to write the prompt:**

1. **State the extension intent first.** Begin with phrases like "Continuing from the previous shot" or "Extend forward from the source video" so the model knows this is a continuation, not a new video.

2. **Describe only the new segment.** Don't re-describe the whole scene. Write what happens in the 5 seconds you're adding, e.g., the character lands, reacts, walks away.

3. **Keep the character and environment consistent.** Reference the same character and outfit from the source ("the same sloth in the cowboy hat"), and stay in the same location and style.

4. **One camera move, one lighting keyword.** Pick a single camera movement (slow push in, steadicam follow, low angle) and one lighting term (golden hour cinematography). One strong keyword beats a pile of adjectives.

5. **Add audio.** Seedance generates sound natively. Describe the music and sound effects at the end ("western arena music swells").

6. **Close with constraints.** End with "No black frames, no text overlays" to keep the output clean.

**Example:**

> Continuing from the previous shot, live-action western rodeo, dusty arena, golden hour. The raging bull calms down and stops, the buzzer rings. The sloth in the cowboy hat hops off the bull's back, lands steadily in the dust, slowly dusts off his hat, then strolls away unhurriedly with a deadpan expression. Slow motion, dust floating in warm sunlight, cheering crowd roars and waves hats in the background. Steadicam follow shot. Western arena music swells. No black frames, no text overlays.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
