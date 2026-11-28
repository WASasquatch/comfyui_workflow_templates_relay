# Camera Control: MiniMax H3 Max

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_max_camera_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_camera_control-1.webp" width="360" alt="Camera Control: MiniMax H3 Max api_minimax_h3_max_camera_control-1.webp">

> Orbit the camera around a still image with MiniMax H3 Max, then put your own music under it. The image is the first frame and the model renders the move to a new azimuth, elevation and distance, inventing whatever the camera uncovers; the graph then rebuilds the clip with a music bed through Get Video Components and Create Video, because the model's own score for a near-static shot comes out as a low rumble.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_camera_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_camera_control.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_camera_control` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, Camera, Video |
| Type | API |
| Date | 2026-11-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 32 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | api_minimax_h3_max_camera_control_input.png |
| input | `LoadAudio` #4 | audio | api_minimax_h3_max_camera_control_music.mp3 |
| output | `SaveVideo` #6 | video | api_minimax_h3_max_camera_control.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CreateVideo` | 1 |  |
| `GetVideoComponents` | 1 |  |
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MinimaxHailuo03MaxCameraControlNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Camera Control: MiniMax H3 Max

**Input Assets**
- [api_minimax_h3_max_camera_control_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_minimax_h3_max_camera_control_input.png) — required workflow input (`input/api_minimax_h3_max_camera_control_input.png`)
- [api_minimax_h3_max_camera_control_music.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_minimax_h3_max_camera_control_music.mp3) — required workflow input (`input/api_minimax_h3_max_camera_control_music.mp3`)

**Move the camera around a still image, then put your own music under it.** The image is the first frame; the node renders the move to a new azimuth, elevation and distance and generates its own ambience. The graph then takes the picture back out of that clip and rebuilds it with a music bed, because the model's own score for a near-static shot comes out as a low rumble.

---

### What this graph does

1. **Load Image**: the opening frame, at least 256 x 256 and an aspect ratio between 0.4 and 2.5.
2. **MiniMax H3 Max Camera Control**: the camera move and the model's own audio.
3. **Get Video Components**: splits the generated clip into frames, audio and fps. Only the frames and the fps are used here.
4. **Load Audio**: the music bed.
5. **Create Video**: rebuilds the clip from the frames at the same fps and attaches the music instead of the model audio.
6. **Save Video**: writes `api_minimax_h3_max_camera_control.mp4`.

To keep the model's ambience as well, route `Get Video Components` audio into `Audio Concat` with the music and feed the result into `Create Video`.

### Prompt format

The node reads MiniMax H3 prompts, so the prompt follows the official I2VA structure rather than a plain sentence:

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, ... The camera holds an Arc Shot with small amplitude at slow speed ...

overall_soundscape: ...

non_diegetic_music: ...
```

- The alignment line stays first.
- `integrated_multimodal_description` carries the visual timeline, the camera vocabulary (`Arc Shot`, `Push In`, `Tracking Shot`, with `small/large amplitude` and `slow/fast speed`) and any dialogue in `<d>[English] ...</d>`.
- `overall_soundscape` holds ambience and physical sound, `non_diegetic_music` the audience-only score. Write `N/A` when you intend to add music afterwards, as this template does.

### Parameters

| Widget | What it does |
|---|---|
| `azimuth` | Horizontal orbit in degrees, `-360` to `360`; positive moves the camera right. |
| `elevation` | End angle above or below the subject, `-90` to `90`; positive looks down. |
| `distance` | End distance relative to the start: `1` keeps it, below `1` pushes in, above `1` pulls back. |
| `duration` | 1 to 15 seconds; this example runs 5. |
| `resolution` | `480P`, `768P` or `1080P`. |
| `prompt_expansion_mode` | `disabled`, `balanced` or `quality`. |

### Measured on this graph

`api_minimax_h3_max_camera_control_input.png` (1024 x 1024, a woman in a red coat under neon) produced 768 x 768, 124 frames, 5.17 s at 24 fps. With the music bed attached the track measures a 4.7 kHz spectral centroid with 59 percent of its energy above 2 kHz; the same clip with only the model audio measured 718 Hz with 9 percent.

### Gotchas

- `azimuth` is a target, not a guarantee: a 90 degree request often lands between 30 and 90 degrees.
- A camera-info node connected to `camera_info` overrides `azimuth` and `elevation`.
- The image aspect ratio must stay between 0.4 and 2.5.
- `Create Video` re-encodes the frames, so the clip loses the model's audio unless you mix it back in with `Audio Concat`.
- Trim the music to the clip length; `Create Video` runs until the shorter of the two ends.

</details>
