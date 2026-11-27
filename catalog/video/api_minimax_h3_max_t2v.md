# MiniMax H3 Max: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_max_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_t2v-1.webp" width="360" alt="MiniMax H3 Max: Text to Video api_minimax_h3_max_t2v-1.webp">

> Generate polished, prompt-faithful video from text using MiniMax H3 Max, producing a single finished video clip with no input files required. Ideal for rapid concept exploration, cinematic text-to-video scenes, and high-throughput creative iteration where speed and visual quality matter.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_t2v.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-09-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.3 |
| Usage | 64 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #11 | video | api_minimax_h3_max_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 |  |
| `MarkdownNote` | 2 |  |
| `PrimitiveBoolean` | 2 |  |
| `SaveVideo` | 2 |  |
| `MinimaxHailuo03ContextIRNode` | 1 |  |
| `MinimaxHailuo03RegenerateNode` | 1 |  |
| `MinimaxHailuo03TextToVideoNode` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Guide</summary>

## How this graph is wired

This is a MiniMax H3 Max **text-to-video** template. It has **one required path** and **two optional stages**. You choose whether to run the optional stages. Both start **off**.

On the canvas, two nodes are marked **red**. Those are **Switch** nodes. Each is the on/off gate for an optional stage, driven by a boolean in the **Feature Flags** group.

### 1. Video generation (required)

**MiniMax H3 Text to Video** is the core. It always runs. Feed it **Text (Prompt)**. The first **Save Video** is the first-pass output.

### 2. Prompt enhance (optional)

**Boolean (Prompt Enhance)** feeds the red **Switch** in **Prompt Enhancer (Optional)**.

- Set it to `true` to rewrite the prompt with **MiniMax H3 Context IR (Prompt Enhancer)** before generation.
- Leave it `false` to send your raw prompt straight to video generation.

### 3. Video upscale (optional)

**Boolean (Upscale to 2K)** feeds the red **Switch** in **Upscale Video to 2K (Optional)**.

- Set it to `true` to run **MiniMax H3 Regenerate to 2K** on the first-pass video.
- Leave it `false` to save the first-pass video as-is.

Upscale **only accepts 768P** source video. If you turn this stage on, generate at **768P**. Other resolutions are not supported by **MiniMax H3 Regenerate to 2K**.

You can enable section 2, section 3, both, or neither.

### Duration must match

Keep **duration** the same on every MiniMax node you actually use (generation, prompt enhance, and upscale). The clip length must match across those stages. If one node is 5s and another is 6s, enhance or upscale will be out of sync with the generated video.

### Extra inputs must be duplicated

The generate node is text-only. **MiniMax H3 Context IR (Prompt Enhancer)** and **MiniMax H3 Regenerate to 2K** still accept extra context (first/last frame, extra images, reference video, audio).

Those two optional nodes do **not** share extra context automatically. If you add extra input nodes and turn on prompt enhance or upscale, **plug the same wires into both**:

- **MiniMax H3 Context IR (Prompt Enhancer)**, so prompt enhance sees that context
- **MiniMax H3 Regenerate to 2K**, so upscale sees that context

If you only wire extras into one of them, the other stage will run without that context and the result will drift.

</details>

<details><summary>Note: Requirement for Video Upscale</summary>

Upscale only accepts **768P** source video. Generate at 768P if you turn on **Boolean (Upscale to 2K)**. Other resolutions are not supported.

</details>
