# Seedance2.0 Real Human: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_real_human-1.webp" width="360" alt="Seedance2.0 Real Human: Reference to Video api_seedance2_0_r2v_real_human-1.webp">

> Upload a reference video of a real person for identity verification. Use your own photo to validate and generate a personalized video output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_real_human.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_r2v_real_human.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_r2v_real_human` |
| Category | Foundation › Video |
| Media type | image |
| Models | Seedance 2.0 |
| Tags | API, Video, Reference to Video |
| Type | API |
| Date | 2026-04-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 57 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | real_human_demo.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `SaveText` | 2 |  |
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `ByteDanceCreateImageAsset` | 1 | comfy-core |
| `ByteDanceCreateVideoAsset` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: group_id</summary>

### Group ID Explanation  
- **Purpose**: Groups same-person real-human assets for backend recognition.  
- **Generation**: Auto-generated after the first verification via the "ByteDance Create Image/Video Asset" node.  
- **Usage**: Save the Group ID. For future same-person assets, entering this ID skips verification.

</details>

<details><summary>MarkdownNote</summary>

### [How to Use Real-Human Assets for Seedance2.0](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)

To comply with the model provider’s legal requirements, real-human assets must be verified before use.  

1. **First-Time Asset Upload & Verification**: Use "Load Image" to upload a real-human image. Run the workflow; the "ByteDance Create Image Asset" or "ByteDance Create Video Asset" node generates a verification link. Complete verification to obtain an Asset ID and a Group ID.  
2. **Reuse the Same Person’s Assets**: Save the Group ID. For future uploads of the same person’s images/videos, enter the saved Group ID in the "Create Image/Video Asset" node to skip verification, since the person is already verified.  
3. **Video Generation**: Use the Asset ID in the "ByteDance Seedance 2.0" node to generate a video with a real human as a reference.
---
- A Group ID verified by a single account is usable only by that account and does not support cross-account use.
- Please ensure the image/video used to create assets contains only one character

</details>

<details><summary>Note: Input Limit</summary>

The `image` and `video` inputs do not support real humans.
To use real human images or videos, first generate an asset ID via **ByteDance Create Image/Video Asset**.

Asset limits:
- Images: up to 9
- Videos: up to 3
- Audio: up to 3

</details>
