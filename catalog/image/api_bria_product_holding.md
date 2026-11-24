# Bria: Product Holding

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_product_holding-1.webp" width="360" alt="Bria: Product Holding api_bria_product_holding-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_product_holding-2.webp" width="360" alt="Bria: Product Holding api_bria_product_holding-2.webp">

> Place a product into the hands of the person in a photo with Bria. One person photo plus one to three product shots is enough for a lifestyle image in which the face, pose and background stay untouched and the product is held naturally. Ideal for e-commerce and social content that would otherwise need a shoot.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_product_holding.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_product_holding.json)

## Details

| | |
|---|---|
| Name | `api_bria_product_holding` |
| Category | Foundation › Image |
| Media type | image |
| Models | BRIA |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 0 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | bria_holding_person.png |
| input | `LoadImage` #3 | image | bria_holding_product.png |
| output | `SaveImage` #5 | image | api_bria_product_holding.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `BriaProductHolding` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Bria: Product Holding

Put a product into the person's hands. Bria keeps the face, pose and background of the person photo and renders the product held naturally, so a phone snapshot plus a product shot is enough for a lifestyle image. The result comes back at roughly one megapixel.

## Input Asset

- [bria_holding_person.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/bria_holding_person.png)
- [bria_holding_product.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/bria_holding_product.png)

## Parameters

- `product_images` takes 1 to 3 images of the same product: the product, its packaging, another angle or a companion item. The node starts with one product socket, and the + button on the node adds more.
- `instruction` is optional extra direction on top of Bria's built-in one, such as `hold the bag in one hand` or `face the label to the camera`. Left empty, the product is simply placed in a hand.
- Better results come from a person photo where the hands are already visible and empty, which gives Bria room to place the product.
- `aspect_ratio` at `auto` keeps the framing of the person photo; a fixed ratio returns 0.6 to 1 megapixel.
- When the person already holds something similar, the product replaces it instead of being added next to it.
- This node only returns an image, so it is connected to Save Image.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
