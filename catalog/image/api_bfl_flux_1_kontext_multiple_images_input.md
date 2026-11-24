# Flux.1 Kontext Multiple Image Input

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux_1_kontext_multiple_images_input)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux_1_kontext_multiple_images_input-1.webp" width="360" alt="Flux.1 Kontext Multiple Image Input api_bfl_flux_1_kontext_multiple_images_input-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux_1_kontext_multiple_images_input-2.webp" width="360" alt="Flux.1 Kontext Multiple Image Input api_bfl_flux_1_kontext_multiple_images_input-2.webp">

> Input multiple images and edit them with Flux.1 Kontext.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux_1_kontext_multiple_images_input.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux_1_kontext_multiple_images_input.json)
- [Tutorial](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)

## Details

| | |
|---|---|
| Name | `api_bfl_flux_1_kontext_multiple_images_input` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.1 Kontext, FLUX |
| Tags | API, Image Edit, Image |
| Type | API |
| Date | 2025-05-29 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.40 |
| Usage | 17 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #84 | image | api_bfl_flux_1_kontext_multiple_images_input_girl.jpg |
| input | `LoadImage` #91 | image | api_bfl_flux_1_kontext_multiple_images_input_sofa.jpg |
| input | `LoadImage` #96 | image | api_bfl_flux_1_kontext_multiple_images_input_dog.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `ImageStitch` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `FluxKontextProImageNode` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview) 

To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>

<details><summary>Flux Kontext Prompt Techniques</summary>

### 1. Basic Modifications
- Simple and direct: `"Change the car color to red"`
- Maintain style: `"Change to daytime while maintaining the same style of the painting"`

### 2. Style Transfer
**Principles:**
- Clearly name style: `"Transform to Bauhaus art style"`
- Describe characteristics: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
- Preserve composition: `"Change to Bauhaus style while maintaining the original composition"`

### 3. Character Consistency
**Framework:**
- Specific description: `"The woman with short black hair"` instead of "she"
- Preserve features: `"while maintaining the same facial features, hairstyle, and expression"`
- Step-by-step modifications: Change background first, then actions

### 4. Text Editing
- Use quotes: `"Replace 'joy' with 'BFL'"`
- Maintain format: `"Replace text while maintaining the same font style"`

## Common Problem Solutions

### Character Changes Too Much
❌ Wrong: `"Transform the person into a Viking"`
✅ Correct: `"Change the clothes to be a viking warrior while preserving facial features"`

### Composition Position Changes
❌ Wrong: `"Put him on a beach"`
✅ Correct: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### Style Application Inaccuracy
❌ Wrong: `"Make it a sketch"`
✅ Correct: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## Core Principles

1. **Be Specific and Clear** - Use precise descriptions, avoid vague terms
2. **Step-by-step Editing** - Break complex modifications into multiple simple steps
3. **Explicit Preservation** - State what should remain unchanged
4. **Verb Selection** - Use "change", "replace" rather than "transform"

## Best Practice Templates

**Object Modification:**
`"Change [object] to [new state], keep [content to preserve] unchanged"`

**Style Transfer:**
`"Transform to [specific style], while maintaining [composition/character/other] unchanged"`

**Background Replacement:**
`"Change the background to [new background], keep the subject in the exact same position and pose"`

**Text Editing:**
`"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Remember:** The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.

</details>
