# Bria: Virtual Try-On

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_virtual_try_on)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_virtual_try_on-1.webp" width="360" alt="Bria: Virtual Try-On api_bria_virtual_try_on-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_virtual_try_on-2.webp" width="360" alt="Bria: Virtual Try-On api_bria_virtual_try_on-2.webp">

> Dress the person in a photo with a garment from a separate product shot using Bria. One person photo plus one to three garments or accessories produces a worn look in which the face, pose and background stay untouched and the garment is refitted to the body. Ideal for fashion catalogs and lookbooks without a photoshoot.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_virtual_try_on.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_virtual_try_on.json)

## Details

| | |
|---|---|
| Name | `api_bria_virtual_try_on` |
| Category | Foundation › Image |
| Output | image |
| Models | BRIA |
| Tags | API, Fashion, Image, Image Edit |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 83 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | bria_tryon_man.png |
| input | `LoadImage` #3 | image | bria_tryon_shirt.png |
| output | `SaveImage` #5 | image | api_bria_virtual_try_on.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `BriaVirtualTryOn` | 1 |  |
| `ImageCompare` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Bria: Virtual Try-On

Put a garment from a product photo onto the person. Bria keeps the face, pose and background of the person photo and refits the garment to the body, so a catalog or flat-lay shot becomes a worn look without a photoshoot. The result comes back at roughly one megapixel.

## Input Asset

- [bria_tryon_man.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/bria_tryon_man.png)
- [bria_tryon_shirt.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/bria_tryon_shirt.png)

## Parameters

- `garment_images` takes 1 to 3 garments or accessories worn together, and each one replaces the matching item the person already wears. The node starts with one garment socket, and the + button on the node adds more.
- `instruction` is optional extra direction on top of Bria's built-in one, such as `keep the shirt untucked` or `roll the sleeves up`. Left empty, the garment is simply worn as shown.
- Two garments are combined into one layered outfit, so a top and a skirt can go in together instead of running the node twice.
- `aspect_ratio` at `auto` keeps the framing of the person photo; a fixed ratio returns 0.6 to 1 megapixel.
- A garment photographed on a hanger or laid flat works as well as one worn by a model.
- This node only returns an image, so it is connected to Save Image.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
