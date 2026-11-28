# Kling 4.0: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling4_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_r2v-1.webp" width="360" alt="Kling 4.0: Reference to Video api_kling4_r2v-1.webp">

> Hold a character and a location from two reference images and shoot a three-shot fashion fragment between them: an extreme close-up with a snap zoom, a mid-hall turn with a whip-pan, and a 120-degree orbit under the arched window. Each cut lands on a new position inside the same room, with two hard cuts in five seconds and stereo audio generated for the space.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_r2v.json)

## Details

| | |
|---|---|
| Name | `api_kling4_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 4.0 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 387 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | kling4_r2v_brutalist_hall.png |
| input | `LoadImage` #5 | image | kling4_r2v_woman_copper_bob.png |
| output | `SaveVideo` #4 | video | api_kling4_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `Kling4ReferenceToVideoNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Two References, Three Shots</summary>

**Input Assets**

- [kling4_r2v_woman_copper_bob.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kling4_r2v_woman_copper_bob.png) — character reference: face, hair, wardrobe
- [kling4_r2v_brutalist_hall.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kling4_r2v_brutalist_hall.png) — location reference: concrete hall, arched window, god-ray

## Two references, two jobs

`@Image1` owns the person: copper-red bob, freckles, burgundy lips, camel leather trench, black turtleneck, wide black trousers, boots — each named, each pinned with `keep … exactly as they are`. `@Image2` owns the room: dark concrete walls, stone bench, arched window, the hard golden beam and the dust in it, plus `do not change the hall` so the model does not redecorate the location it was given.

A reference pins an identity and a place; it does not pin blocking. That is why the prompt asks for the positions in words — close-up in place, then `standing mid-hall beside the stone bench (new position)`, then `centred under the arched window (new position)`. Without that sentence the model keeps her standing exactly where the reference image has her and the cut lands on the same framing twice.

## Three shots in five seconds

- **0–1.5 s** — extreme close-up of her face filling the frame, rim light from the beam on hair and cheek, a small confident almost-smile, a tiny chin tilt, then a snap zoom into the eyes and a hard hold.
- **1.5–3.2 s** — hard cut to mid-hall inside the beam: she turns on her heel, the trench flares, two sharp steps toward camera, and a whip-pan that travels with her motion and stops.
- **3.2–5 s** — hard cut under the arched window: medium three-quarter, arms relaxed, a smooth 120° orbit right around her, dust sparkling in the beam, ending on a clean beauty frame.

Every shot owns its camera move — the shot list says `never one continuous slow pan` explicitly, because left alone the model averages three moves into one drift. Keep the shots few and give each one a different idea; 720p, five seconds, seed 42.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_Frontend/issues](https://github.com/Comfy-Org/ComfyUI_Frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
