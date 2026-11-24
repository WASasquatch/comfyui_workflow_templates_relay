# Tencent: Hy4

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tencent_hy4)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy4-1.webp" width="360" alt="Tencent: Hy4 api_tencent_hy4-1.webp">

> Tencent HY4 reads one reference image and writes the text you ask for: art-directed prompts, detailed captions, or chart and diagram breakdowns, in a single pass. Long-context reasoning and tool use make it a good fit for research write-ups, agent scripts, and batch creative ideation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy4.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tencent_hy4.json)

## Details

| | |
|---|---|
| Name | `api_tencent_hy4` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Hy4 |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-11-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.0 |
| Usage | 50 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | blue_poppies_field.png |

## Subgraphs

- **Format Output** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringConcatenate` | 3 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |
| `TencentHyNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Hy4: Image to Prompt

**Input Assets**
- [blue_poppies_field.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/blue_poppies_field.png) — required workflow input (`input/blue_poppies_field.png`)

Turn a reference image into a reusable prompt. **Tencent HY** (Hy4) reads `Load Image` plus the instruction in **Text (User Prompt)** and writes back a prompt you can paste into any generator. `Preview as Text` shows the reply; **Format Output** wraps it into a text file.

- Edit **Text (User Prompt)** to choose what to extract: subject, composition, lighting, colour, style.
- Hy4 accepts up to 20 images per request; this graph wires one.
- Output: `Hy4/Tencent_Hy4`.

</details>
