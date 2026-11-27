# Seedance2.5 Draft: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_draft_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_t2v-1.webp" width="360" alt="Seedance2.5 Draft: Text to Video api_seedance2_5_draft_t2v-1.webp">

> Generate draft preview videos from text prompts using Seedance 2.5's two-phase draft mode: stage one turns your prompt into a fast, low-cost 480p preview plus a reusable draft task ID, and stage two renders the 1080p final from that ID. Ideal for storyboard testing, rapid creative iteration, and budget-conscious production workflows.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_draft_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_draft_t2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_draft_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API |
| Type | API |
| Date | 2026-09-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.3 |
| Usage | 21 |
| Nodes | 6 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 2 |  |
| `ByteDance2DraftToFinalVideoNode` | 1 |  |
| `ByteDance2TextToVideoNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

**Seedance 2.5 Draft mode** renders a fast, low-cost 480p preview so you can iterate on a prompt before committing to a full render. This workflow runs that in two stages.

**Stage 1: Create and preview the draft video**

1. On the **ByteDance Seedance 2.5 Text to Video** node, keep **Seedance 2.5 Draft** as the model, write your prompt, and run the workflow. You get the 480p preview plus its `draft_task_id`, which the **Save Text** node writes to a .txt file in the output folder.

2. Adjust the prompt and rerun until you like the draft. Once you do, leave this stage bypassed: if the draft node runs again it creates a new draft instead of reusing the one you reviewed.

**Stage 2: Render the final video from the draft**

3. Select the nodes in the **Stage 1** group and press `Ctrl+B` to bypass them.

4. Select the nodes in the **Stage 2** group and press `Ctrl+B` to enable them again.

5. Paste the `draft_task_id` from the saved .txt file into the `draft_task_id` field on the **ByteDance Seedance 2.5 Draft to Final Video** node, then run the workflow. The final 1080p render keeps the draft's prompt, duration, aspect ratio, and audio setting, so there is nothing to re-enter.

Drafts are kept for 7 days, so render the final within that window.

</details>
