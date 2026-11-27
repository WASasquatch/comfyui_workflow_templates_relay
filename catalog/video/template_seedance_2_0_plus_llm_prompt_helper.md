# Seedance 2.0 + LLM Prompt Helper

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_seedance_2_0_plus_llm_prompt_helper)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance_2_0_plus_llm_prompt_helper-1.webp" width="360" alt="Seedance 2.0 + LLM Prompt Helper template_seedance_2_0_plus_llm_prompt_helper-1.webp">

> Upload two reference images and input a short text description. Generate a detailed Seedance 2.0-style prompt automatically with an LLM helper.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance_2_0_plus_llm_prompt_helper.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_seedance_2_0_plus_llm_prompt_helper.json)

## Details

| | |
|---|---|
| Name | `template_seedance_2_0_plus_llm_prompt_helper` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini-3.1-Pro, Seedance 2.0 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-05-10 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.36.0 |
| Usage | 10 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #352 | image | freezer.png |
| input | `LoadImage` #356 | image | snowboarder.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `ByteDance2ReferenceNodeV2` | 1 | comfy-core |
| `GeminiNodeV3` | 1 | comfy-core |
| `ImageStitch` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Workflow Instructions

1. Upload Reference Images  (e.g., location, subject, or style).

2. (Optional) Use the LLM for Prompt Generation  
The LLM can help generate a Seedance 2.0–style prompt based on your inputs.  
- Select the Seedance node and press Ctrl + B to bypass it (so it doesn’t run).  
- Click Run to execute the LLM.

3. Guide Google Gemini  
When using the Google Gemini node, provide a clear description of what you want, including the duration (time).  
Gemini will generate a Seedance 2.0–style prompt based on your input.

4. Review and Apply the Prompt  
- Once you’re happy with the generated prompt, select the Google Gemini node and press Ctrl + B to bypass it.  
- Go back to the Seedance node and press Ctrl + B again to enable it.  
- Paste the generated prompt into the prompt field.

5. Adjust Settings  
Set your desired resolution, aspect ratio, and video duration in the Seedance node.

6. Generate the Video  
Run the workflow again to generate your final output.

</details>
