# Seedance2.5 Draft: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_draft_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_i2v-1.webp" width="360" alt="Seedance2.5 Draft: Image to Video api_seedance2_5_draft_i2v-1.webp">

> Generate draft preview videos from a first frame image using Seedance 2.5's two-phase draft mode: stage one turns your image into a fast, low-cost 480p preview plus a reusable draft task ID, and stage two renders the 1080p final from that ID. Ideal for testing motion, camera and scene ideas on a still before committing to a full-quality render.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_draft_i2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_draft_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-09-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.3 |
| Usage | 142 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #784 | image | friends_enjoying_boba.png |
| output | `SaveVideo` #775 | video | api_seedance2_5_draft_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 2 |  |
| `ByteDance2DraftToFinalVideoNode` | 1 |  |
| `ByteDance2FirstLastFrameNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input asset

- [friends_enjoying_boba.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/friends_enjoying_boba.png)

## Guide

**Seedance 2.5 Draft mode** renders a fast, low-cost 480p preview so you can iterate on a prompt before committing to a full render. This workflow runs that in two stages.

**Stage 1: Create and preview the draft video**

1. Load your first frame in **Load Image** and keep **Seedance 2.5 Draft** as the model on the **ByteDance Seedance 2.5 First-Last-Frame to Video** node. Write your prompt, then run the workflow: you get the 480p preview plus its `draft_task_id`, which the **Save Text** node writes to a .txt file in the output folder. Connect a last frame on the node as well if you want to control the ending.

2. Adjust the prompt or the first frame and rerun until you like the draft. Once you do, leave this stage bypassed: if the draft node runs again it creates a new draft instead of reusing the one you reviewed.

**Stage 2: Render the final video from the draft**

3. Select the nodes in the **Stage 1** group and press `Ctrl+B` to bypass them.

4. Select the nodes in the **Stage 2** group and press `Ctrl+B` to enable them again.

5. Paste the `draft_task_id` from the saved .txt file into the `draft_task_id` field on the **ByteDance Seedance 2.5 Draft to Final Video** node, then run the workflow. The final 1080p render keeps the draft's prompt, first frame, duration, aspect ratio, and audio setting, so there is nothing to re-enter.

Drafts are kept for 7 days, so render the final within that window.

</details>
