# Aspect Ratio Reframe: MiniMax H3 Max

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_reframe-1.webp" width="360" alt="Aspect Ratio Reframe: MiniMax H3 Max api_minimax_h3_max_reframe-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_reframe-2.webp" width="360" alt="Aspect Ratio Reframe: MiniMax H3 Max api_minimax_h3_max_reframe-2.webp">

> Reframe a clip to a new aspect ratio with MiniMax H3 Max: the source keeps its position, timing and audio, and the model generates the surrounding picture instead of cropping the subject. Choose 16:9, 9:16, 1:1, 4:3, 3:4, 21:9 or 9:21 at 480P to 1080P and guide the new area with a prompt. Ideal for turning a vertical social clip into a horizontal edit, or filling a wide frame from a square source.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_reframe.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_reframe.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_reframe` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | MiniMax H3 |
| Tags | API, Outpainting, Video |
| Type | API |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 0 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | futurist_pilot.mp4 |
| output | `SaveVideo` #3 | video | api_minimax_h3_max_reframe.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MinimaxHailuo03MaxReframeVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Aspect Ratio Reframe: MiniMax H3 Max

Reframes a clip to a different aspect ratio without cropping. The source sits in place on the new canvas at its original proportions and H3 Max generates the area around it, so length, motion and audio stay untouched.

**Graph**

1. **Load Video**: the source clip, 0.5 to 300 seconds.
2. **MiniMax H3 Max Reframe Video**: fits the clip on the `aspect_ratio` canvas and generates the surroundings.
3. **Save Video**: writes the MP4.

**Input Assets:** [futurist_pilot.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/futurist_pilot.mp4) — a 5.17 second vertical (576 x 736) two-shot demo.

### Controls

| Control | What it does |
|---|---|
| `aspect_ratio` | Target canvas: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` or `9:21` |
| `resolution` | `480P`, `768P` or `1080P` |
| `prompt` | Optional: what should continue outside the original frame |
| `seed` | The same prompt and seed give similar, not identical, results |

### Prompting

Describe what continues outside the frame, not what is inside it, and cover every shot if the clip has more than one. The demo prompt was: "Continue what is already behind the subject on both sides: the pale gradient backdrop in the opening shot and the hangar corridor with its ceiling light strips in the closing shot, no new props, keep the pilot centred." Leaving `prompt` empty lets the model infer the surroundings from each frame.

</details>
