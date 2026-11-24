# MiniMax H3 Max: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_minimax_h3_max_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_r2v-1.webp" width="360" alt="MiniMax H3 Max: Reference to Video api_minimax_h3_max_r2v-1.webp">

> Generate video from an image reference using MiniMax H3 Max, which animates your still frame while preserving its composition, visual identity, and aspect ratio. The model generates faster than real time with strong prompt adherence and polished cinematic motion. Ideal for bringing character art to life, animating product shots, and creating video from concept images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_minimax_h3_max_r2v.json)

## Details

| | |
|---|---|
| Name | `api_minimax_h3_max_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-09-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.3 |
| Usage | 276 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | burdened_warrior_in_dreamscape.png |
| output | `SaveVideo` #11 | video | api_minimax_h3_max_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `ComfySwitchNode` | 2 |  |
| `PrimitiveBoolean` | 2 |  |
| `SaveVideo` | 2 |  |
| `LoadImage` | 1 |  |
| `MinimaxHailuo03ContextIRNode` | 1 |  |
| `MinimaxHailuo03ReferenceNode` | 1 |  |
| `MinimaxHailuo03RegenerateNode` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Guide</summary>

## How this graph is wired

This is a MiniMax H3 Max **reference-to-video** template. It has **one required path** and **two optional stages**. You choose whether to run the optional stages. Both start **off**.

On the canvas, two nodes are marked **red**. Those are **Switch** nodes. Each is the on/off gate for an optional stage, driven by a boolean in the **Feature Flags** group.

### 1. Video generation (required)

**MiniMax H3 Reference to Video** is the core. It always runs. Feed it **Text (Prompt)** and your references (this template starts with **Load Image** as image_1). You can add more images, a reference video, or audio. The first **Save Video** is the first-pass output.

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

The generate node, the prompt-enhance node, and the upscale node do **not** share extra context automatically.

**Load Image** is already wired into all three as image_1. If you add more inputs (another **Load Image**, a reference video, audio, or any extra output you plug into generation), **also plug the same wires into**:

- **MiniMax H3 Context IR (Prompt Enhancer)**, so prompt enhance sees the same references
- **MiniMax H3 Regenerate to 2K**, so upscale sees the same references

If you only wire extras into generation, enhance and upscale will run without that context and the result will drift.

</details>

<details><summary>Note: Requirement for Video Upscale</summary>

Upscale only accepts **768P** source video. Generate at 768P if you turn on **Boolean (Upscale to 2K)**. Other resolutions are not supported.

</details>

<details><summary>Note: Input Assset</summary>

## Input Asset

- [burdened_warrior_in_dreamscape.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/burdened_warrior_in_dreamscape.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
