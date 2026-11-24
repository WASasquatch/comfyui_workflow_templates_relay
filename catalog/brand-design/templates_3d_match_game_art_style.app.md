# Game Asset Style Transfer Sprite Generator

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_3d_match_game_art_style.app-1.webp" width="360" alt="Game Asset Style Transfer Sprite Generator templates_3d_match_game_art_style.app-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_3d_match_game_art_style.app-2.webp" width="360" alt="Game Asset Style Transfer Sprite Generator templates_3d_match_game_art_style.app-2.webp">

> Use an outline reference, and a style reference as input to generate 2D sprite as model textures. Useful for background set dressing in 2D/2.5D game.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_3d_match_game_art_style.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_3d_match_game_art_style.app.json)

## Details

| | |
|---|---|
| Name | `templates_3d_match_game_art_style.app` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Game, Style Reference |
| Type | API |
| Date | 2026-03-06 |
| Author | shane |
| Min ComfyUI version | 0.9.0 |
| Usage | 14 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | game_style.png |
| input | `LoadImage` #2 | image | gas_lamp.png |
| output | `SaveImage` #5 | image | templates_3d_match_game_art_style-1.png |
| output | `SaveImage` #3 | image | templates_3d_match_game_art_style-2.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveStringMultiline` | 3 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `StringConcatenate` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `RecraftRemoveBackgroundNode` | 1 | comfy-core |
