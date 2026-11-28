# Mirelo SFX 2.0: Text to SFX

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_mirelo_text_to_sfx)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_text_to_sfx-1.webp" width="360" alt="Mirelo SFX 2.0: Text to SFX api_mirelo_text_to_sfx-1.webp">

> Generate sound effects from a text prompt with Mirelo sfx-2.0: name the sound, its material, space and intensity in one line and get a 48 kHz mono audio file, up to 10 minutes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_text_to_sfx.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_mirelo_text_to_sfx.json)

## Details

| | |
|---|---|
| Name | `api_mirelo_text_to_sfx` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Mirelo |
| Tags | Text to Audio, Audio, API |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 139 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `MireloTextToSFX` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Prompt Guide</summary>

## Mirelo Text → SFX — Prompt Guide (sfx-2.0)

Generate SFX from text. The **prompt is required**. No video — content and length come from your prompt + duration.

## Formula

One short line that names the **sound**, not a story:

**Source + material/surface + space/distance + intensity**  
(optional: rhythm, layers, mic distance)

| Part | Examples |
| --- | --- |
| Source | rain, footsteps, hammer, door latch, whoosh, sizzle |
| Material | tin roof, wet concrete, wood floor, leather, gravel |
| Space | close mic, distant, small room, outdoors, large hall |
| Intensity | soft, heavy, sharp, muted, ringing |

## Good prompts

- `Heavy rain on a tin roof with distant thunder`
- `Soft footsteps on wood floor in a small quiet room`
- `Sharp knife chop on a wooden cutting board, close mic`
- `Car engine idle then short acceleration whoosh, outdoors`
- `Ceramic cup clink on saucer, soft café ambience underneath`
- `Metal door slam in a concrete hallway with short echo`
- `Crackling campfire with occasional wood pop, outdoors at night`

## Weak → better

| Weak | Better |
| --- | --- |
| `epic cinematic vibe` | `Deep low whoosh then heavy impact on metal, large hall` |
| `scary atmosphere` | `Distant creaking wood floorboards, soft wind under a door` |
| `a man walks into a bar…` | `Bar door open, footsteps on wood, glass clink on counter` |
| `upbeat music` | Wrong product — or `crowd chatter and glass clinks, no music` |

## Negative prompt (optional)

Comma-separated leave-outs. Experimental / often weak on Text→SFX — use as a nudge:

`music, speech, wind, birds, crowd`

Example: prompt `Heavy rain on a metal roof` · negative `music, speech, thunder`

## Tips

1. Concrete nouns you can hear beat abstract mood words.
2. One main event per prompt; add layers only if needed (`…, soft ambience underneath`).
3. Prefer one clear line over a paragraph.
4. Match **duration** to the event (a hit ≠ 30 s of rain).
5. Run **2–4 variants** and pick by ear; change one dimension at a time when iterating.

## Paste-ready template note

> Describe the *sound*, not the story. Name source, material/surface, space/distance, and intensity in one short line.  
> Example: `Heavy rain on a tin roof with distant thunder`.  
> Optional negative: `music, speech, wind`.

</details>
