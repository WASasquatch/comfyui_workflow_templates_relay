# Storyboard To Video - Seedance 2.0

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_seedance2_storyboard_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_storyboard_to_video-1.webp" width="360" alt="Storyboard To Video - Seedance 2.0 template_seedance2_storyboard_to_video-1.webp">

> Generate an 8-panel storyboard from a simple text prompt, then use that storyboard as the foundation for Seedance 2.0. The storyboard provides a visual blueprint for the sequence, allowing you to guide the video with more control over the action, camera angles, composition, and overall storytelling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_storyboard_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_seedance2_storyboard_to_video.json)

## Details

| | |
|---|---|
| Name | `template_seedance2_storyboard_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-06-15 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.35.2 |
| Usage | 52 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | storyboard_input.png |
| input | `LoadImage` #10 | image | ninja.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNodeV3` | 2 |  |
| `LoadImage` | 2 |  |
| `MarkdownNote` | 2 |  |
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `ImageStitch` | 1 |  |
| `OpenAIGPTImageNodeV2` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImage` | 1 |  |
| `SaveVideo` | 1 |  |
| `StringConcatenate` | 1 |  |

## Notes embedded in the workflow

<details><summary>Step 1</summary>

## Step 1: Generate the Storyboard

Try to use the [Partial Execution](https://docs.comfy.org/interface/features/partial-execution) to run different steps

Before generating the storyboard, make sure the **Seedance 2.0** group is bypassed. Right-click anywhere inside the **Seedance 2.0** group and select **Bypass Group Nodes**.

Enter a scene description and run the storyboard workflow to generate an 8-panel storyboard.

</details>

<details><summary>Step 2</summary>

## Step 2: Animate with Seedance 2.0

Once the storyboard has been generated, bypass the storyboard generator group and remove the bypass from the **Seedance 2.0** group.

Next to the field labeled **Image**, click the image selector. A window will appear showing previously generated images. Select the storyboard you generated in Step 1 to load it into **Seedance 2.0**.

Use the lower image input for your subject reference. You can also add additional reference images, such as environment or location images, to help maintain scene consistency throughout the animation.

</details>
