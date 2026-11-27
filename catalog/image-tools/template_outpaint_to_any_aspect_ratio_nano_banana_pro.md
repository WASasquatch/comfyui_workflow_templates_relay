# Outpaint to Any Aspect Ratio - Nano Banana Pro

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_outpaint_to_any_aspect_ratio_nano_banana_pro)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_outpaint_to_any_aspect_ratio_nano_banana_pro-1.webp" width="360" alt="Outpaint to Any Aspect Ratio - Nano Banana Pro template_outpaint_to_any_aspect_ratio_nano_banana_pro-1.webp">

> Upload your image, input your desired aspect ratio and the images position (as a percentage) in the new aspect ratio composite. Uses Nano Banana Pro to generate an outpainted version of your image to fit the new dimensions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_outpaint_to_any_aspect_ratio_nano_banana_pro.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_outpaint_to_any_aspect_ratio_nano_banana_pro.json)

## Details

| | |
|---|---|
| Name | `template_outpaint_to_any_aspect_ratio_nano_banana_pro` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Nano Banana Pro |
| Tags | API, Outpainting |
| Type | API |
| Date | 2026-05-04 |
| Author | hellorob |
| Min ComfyUI version | 0.16.4 |
| Usage | 18 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #130 | image | facing_the_dragon.png |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [controlaltai-nodes](https://registry.comfy.org/nodes/controlaltai-nodes)

## Subgraphs

- **Image Extender** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `GetImageSize` | 2 | comfy-core |
| `EmptyImage` | 1 | comfy-core |
| `FluxResolutionNode` | 1 | controlaltai-nodes |
| `GeminiImage2Node` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageCompositeMasked` | 1 | comfy-core |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `ImageResize+` | 1 | comfyui_essentials |
| `ImageResizeKJv2` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `PreviewImage` | 1 |  |
| `PrimitiveInt` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Outpaint Image to Any Aspect Ratio</summary>

Outpaint a **single image** into any target aspect ratio without cropping. The original pixels stay intact — the new canvas around them is outpainted by **Nano Banana Pro**

## How It Works

1. **Upload an image** (`LoadImage` node)
2. **Select `Image Extender` node inputs**
   - **Image Extender** — pads the original to the target aspect ratio, with you controlling **where** the image sits inside the new canvas (left↔right and top↔bottom percentages, both default to 50% = centered).
      - **aspect_ratio** — pick from the dropdown.
      - **top_or_left_outpaint_pct** — `0` = image hugs left/top, `50` = centered, `100` = hugs right/bottom. Use these to compose how the original sits in the new frame. 

3. **Nano Banana 2 outpaint** — replaces the green region with new image content that continues the input image naturally (sky, ground, walls, whatever fits). Tweak the prompt with specific details if necessary.

## Tips

- **Low contrast = bad inpaint.** If your subject contains a lot of green (plants, a green-screen setup), open the Image Extender subgraph and change the fill color to something that contrasts your subject.
- **Match the subject scale.** If you go from `1:1` → `21:9`, you're asking the model to invent a *lot* of pixels; busy or simple backgrounds (skies, walls) outpaint more reliably than complex scenes.

</details>

<details><summary>Position Control</summary>

## Position

`top_or_left_whitespace_pct` (0–100) biases the input on the slack axis.

- 0 = flush top/left
- 50 = centered (default)
- 100 = flush bottom/right

The active axis is whichever has slack after fitting the input into the target aspect ratio.

</details>

<details><summary>EmptyImage Color</summary>

# `0xRRGGBB` packed as one int                                                                                                                            
                                         
  `65280` = `0x00FF00` = pure green. Same as HTML hex, just decimal.                                                                                                              
                                                                                                                                                                                  
  | Color | Hex | Int |                                                                                                                                                           
  |---|---|---|                                             
  | Black | `0x000000` | `0` |                                                                                                                                                    
  | White | `0xFFFFFF` | `16777215` |                       
  | Red   | `0xFF0000` | `16711680` |                                                                                                                                             
  | Green | `0x00FF00` | `65280` |
  | Blue  | `0x0000FF` | `255` |

</details>
