# Seedance2.0 Real Human: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_0_flf2v_real_human)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v_real_human-1.webp" width="360" alt="Seedance2.0 Real Human: FLF2V api_seedance2_0_flf2v_real_human-1.webp">

> Upload a reference image of a real person for identity verification and generate a personalized video with first and last frame control using Seedance2.0 FLF2V.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v_real_human.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_flf2v_real_human.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_flf2v_real_human` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, Video, FLF2V |
| Type | API |
| Date | 2026-04-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.2 |
| Usage | 9 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #20 | image | flf2v_demo_first_frame.png |
| input | `LoadImage` #38 | image | flf2v_demo_last_frame.png |
| output | `SaveVideo` #15 | video | api_seedance2_0_flf2v_real_human.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `ByteDanceCreateImageAsset` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `ByteDance2FirstLastFrameNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Guide</summary>

### [How to Use Real-Human Assets for Seedance2.0](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0)

To comply with the model provider’s legal requirements, real-human assets must be verified before use.  

1. **First-Time Asset Upload & Verification**: Use "Load Image" to upload a real-human image. Run the workflow; the "ByteDance Create Image Asset" or "ByteDance Create Video Asset" node generates a verification link. Complete verification to obtain an Asset ID and a Group ID.  
2. **Reuse the Same Person’s Assets**: Save the Group ID. For future uploads of the same person’s images/videos, enter the saved Group ID in the "Create Image/Video Asset" node to skip verification, since the person is already verified.  
3. **Video Generation**: Use the Asset ID in the "ByteDance Seedance 2.0" node to generate a video with a real human as a reference.
---
- A Group ID verified by a single account is usable only by that account and does not support cross-account use.
- Please ensure the image/video used to create assets contains only one character

</details>

<details><summary>Note: group_id</summary>

### Group ID Explanation  
- **Purpose**: Groups same-person real-human assets for backend recognition.  
- **Generation**: Auto-generated after the first verification via the "ByteDance Create Image/Video Asset" node.  
- **Usage**: Save the Group ID. For future same-person assets, entering this ID skips verification.

</details>

<details><summary>Note: Input limit</summary>

1. An access ID is equivalent to an image input.
2. For the first frame, if you use an access ID input, you cannot use an image input simultaneously. The same applies to the last frame.
3. You don't need to use the asset ID for both the first and last frames. This workflow is just an example of how to use real human assets.

</details>
