# Cast Swap: MiniMax H3 Max

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_max_recast)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_recast-1.webp" width="360" alt="Cast Swap: MiniMax H3 Max api_minimax_h3_max_recast-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_recast-2.webp" width="360" alt="Cast Swap: MiniMax H3 Max api_minimax_h3_max_recast-2.webp">

> Swap the people in a finished clip with MiniMax H3 Max Recast: connect up to four reference photos and the model rewrites the cast while keeping the motion, the framing, the cuts and the original audio. Clips run 5 to 30 seconds with no shot longer than 15 seconds, at 480P to 1080P, with an option for more natural skin and blending. Ideal for recasting a shot without a reshoot, localising a presenter, or testing a look with a different face.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_recast.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_recast.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_recast` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, Video, Video Edit |
| Type | API |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 291 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | ad_video_demo.mp4 |
| input | `LoadImage` #2 | image | woman_in_red.png |
| output | `SaveVideo` #4 | video | api_minimax_h3_max_recast.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MinimaxHailuo03MaxRecastNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Cast Swap: MiniMax H3 Max

**Replace the people in a finished shot.** Recast keeps the motion, the framing, the cuts and the original sound, and swaps the people for the ones in your reference photos.

---

### What this graph does

1. **Load Video**: the source clip. It must be 5 to 30 seconds long and no single shot inside it may run longer than 15 seconds.
2. **Load Image**: the replacement person, at least 256 x 256. Connect up to four photos for up to four people: they become `@Image1` to `@Image4` in socket order.
3. **MiniMax H3 Max Recast**: rewrites the people in the clip to match the photos.
4. **Save Video**: writes the MP4.

**Input Assets:** [ad_video_demo.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ad_video_demo.mp4) · [woman_in_red.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/woman_in_red.png)

---

### Writing the prompt

The prompt says who becomes whom and what has to stay in place. Name the photos by their slot, `@Image1` for the first photo connected to the node, then say what the person is doing and what must not change:

- `@Image1 is now the woman in the video: keep her speaking to camera, holding the lipstick up the same way, same bright room with white flowers, same framing and timing.`
- Two people: `@Image1 replaces the presenter and @Image2 replaces the guest, keep the handshake and the pan.`
- Do not describe the look of the new person: costume, hair and accessories follow the reference photo, so a photo of someone in a red suit comes back in a red suit. Spend the prompt on behaviour, blocking and what has to stay.

The prompt is optional, but the swap is much more predictable when it is there.

---

### Controls

| Control | What it does |
|---|---|
| `model` | `MiniMax H3 Max` is the only option on this node |
| `resolution` | `480P`, `768P` or `1080P`, default `768P` |
| `enhance_realism` | More natural skin texture and better blending of the new person into the scene. The demo below was rendered with it on |
| `seed` | Same prompt and seed give similar, not identical, results |

### What the demo run produced

`ad_video_demo.mp4` (1280 x 720, 5.04 seconds) kept its timing and its audio and came back at 1344 x 768 with the presenter replaced by the person in `woman_in_red.png`. The wardrobe followed the reference photo as well, red suit and beret instead of the original green top, and the face stayed stable across all 121 frames with no flicker on the product or the flowers.

### Gotchas

- One photo per person, assigned in socket order. Five photos is over the limit of four.
- Clips shorter than 5 seconds, or with a shot longer than 15 seconds, are rejected before generation.
- The source audio is kept, Recast does not regenerate speech.

</details>
