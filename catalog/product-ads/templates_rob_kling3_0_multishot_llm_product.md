# Kling 3.0: 1 Click Multishot

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_rob_kling3_0_multishot_llm_product)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_kling3_0_multishot_llm_product-1.webp" width="360" alt="Kling 3.0: 1 Click Multishot templates_rob_kling3_0_multishot_llm_product-1.webp">

> Upload a start frame and references of your product. Select total duration and number of shots and automatically generate prompts for each shot.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_kling3_0_multishot_llm_product.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_rob_kling3_0_multishot_llm_product.json)

## Details

| | |
|---|---|
| Name | `templates_rob_kling3_0_multishot_llm_product` |
| Category | Applied › Product & Ads |
| Output | video |
| Models | Kling 3.0 |
| Tags | API, Text to Video, Video |
| Type | API |
| Date | 2026-03-18 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 38 |
| Nodes | 67 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | comfy_gpu_angled.png |
| input | `LoadImage` #8 | image | comfy_gpu_flat.png |
| input | `LoadImage` #12 | image | comfy_gpu_close_up.png |
| output | `SaveVideo` #89 | video | templates_rob_kling3_0_multishot_llm_product.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-string-converter](https://registry.comfy.org/nodes/comfyui-string-converter)
- [was-ns](https://registry.comfy.org/nodes/was-ns)

## Subgraphs

- **Create Prompt** (5 nodes)
- **Extract Prompts** (12 nodes)
- **Resize and Batch Images** (4 nodes)
- **Selected Prompt** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 13 | comfy-core |
| `RegexExtract` | 12 | comfy-core |
| `Reroute` | 12 |  |
| `StringToInt` | 6 | comfyui-string-converter |
| `LoadImage` | 3 | comfy-core |
| `Note` | 2 |  |
| `PrimitiveInt` | 2 | comfy-core |
| `RegexReplace` | 2 | comfy-core |
| `ResizeAndPadImage` | 2 | comfy-core |
| `SomethingToString` | 2 | comfyui-kjnodes |
| `BatchImagesNode` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `GeminiNodeV3` | 1 |  |
| `GetImageSize` | 1 | comfy-core |
| `KlingOmniProImageToVideoNode` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveString` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `StringCompare` | 1 | comfy-core |
| `Text Multiline` | 1 | was-ns |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Shot 1 - 6 Durations (desc order)
```

</details>

<details><summary>Note</summary>

```text
Shot 1 - 6 Prompts (desc order)
```

</details>

<details><summary>MarkdownNote</summary>

# Workflow Instructions

1. Upload start frame and product reference images.
2. Enter your desired values in the **Number of Seconds** node and **Number of Shots** node.
3. Run the workflow to generate the prompts.
4. Once the **Google Gemini** node generates a prompt you like, copy from the **Preview All Prompts** node and paste into the **Prompt Input** node. Then, Bypass all the nodes in the **LLM Generate Each Shots Prompts** group.
5. Run the workflow to view a preview of each shot's correlating prompt and number of seconds in the **Preview Prompts** group.
6. Unbypass **Generate and Save Video** group nodes. **IMPORTANT:** Change the `storyboards` value to the same number of shots you have selected.
7. Run the workflow again to generate the final video.

</details>
