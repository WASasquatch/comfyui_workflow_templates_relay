# Seedance2.5 Draft: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_draft_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_r2v-1.webp" width="360" alt="Seedance2.5 Draft: Reference to Video api_seedance2_5_draft_r2v-1.webp">

> Generate draft preview videos from reference images using Seedance 2.5's two-phase draft mode: stage one turns your references and prompt into a fast, low-cost 480p preview plus a reusable draft task ID, and stage two renders the 1080p final from that ID. Ideal for locking in a character or storyboard reference before committing to a full-quality render.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_draft_r2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_draft_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-09-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.3 |
| Usage | 879 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #788 | image | mech_comic_storyboard.png |
| input | `LoadImage` #795 | image | yellow_mech_character_sheet.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `SaveVideo` | 2 |  |
| `ByteDance2DraftToFinalVideoNode` | 1 |  |
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input assets

- [yellow_mech_character_sheet.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/yellow_mech_character_sheet.png)
- [mech_comic_storyboard.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/mech_comic_storyboard.png)

## Guide

**Seedance 2.5 Draft mode** renders a fast, low-cost 480p preview so you can iterate on a prompt before committing to a full render. This workflow runs that in two stages.

**Stage 1: Create and preview the draft video**

1. Load your reference images in the two **Load Image** nodes and keep **Seedance 2.5 Draft** as the model on the **ByteDance Seedance 2.5 Reference to Video** node. `task_type` stays on **auto**, which generates a new video guided by those references; set it to `edit` or `extend` instead when a reference video is connected. Write your prompt, then run the workflow: you get the 480p preview plus its `draft_task_id`, which the **Save Text** node writes to a .txt file in the output folder.

2. Adjust the prompt or the reference images and rerun until you like the draft. Once you do, leave this stage bypassed: if the draft node runs again it creates a new draft instead of reusing the one you reviewed.

**Stage 2: Render the final video from the draft**

3. Select the nodes in the **Stage 1** group and press `Ctrl+B` to bypass them.

4. Select the nodes in the **Stage 2** group and press `Ctrl+B` to enable them again.

5. Paste the `draft_task_id` from the saved .txt file into the `draft_task_id` field on the **ByteDance Seedance 2.5 Draft to Final Video** node, then run the workflow. The final 1080p render keeps the draft's prompt, references, duration, aspect ratio, and audio setting, so there is nothing to re-enter.

Drafts are kept for 7 days, so render the final within that window.

</details>
