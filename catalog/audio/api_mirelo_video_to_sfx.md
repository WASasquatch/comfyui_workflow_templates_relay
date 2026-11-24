# Mirelo SFX 2.0: Video to SFX

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_mirelo_video_to_sfx)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_video_to_sfx-1.webp" width="360" alt="Mirelo SFX 2.0: Video to SFX api_mirelo_video_to_sfx-1.webp">

> Add picture-locked sound effects to a clip with Mirelo sfx-2.0: the model watches the video and times Foley to on-screen action, keeps speech by default, and saves the SFX track, the speech track and the video carrying the new mix.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_mirelo_video_to_sfx.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_mirelo_video_to_sfx.json)

## Details

| | |
|---|---|
| Name | `api_mirelo_video_to_sfx` |
| Category | Foundation › Audio |
| Output | video |
| Models | Mirelo |
| Tags | Video, Audio, API |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 167 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #7 | video | mage_crash_discovery_video.mp4 |
| output | `SaveVideo` #730 | video | api_mirelo_video_to_sfx.mp4 |

## Subgraphs

- **Video Audio Merger** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `AudioAdjustVolume` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `SaveAudioAdvanced` | 2 |  |
| `AudioMerge` | 1 | comfy-core |
| `ComfySwitchNode` | 1 |  |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `MireloVideoToSFX` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Video to SFX Guide</summary>

## Mirelo Video → Synced SFX — Guide (sfx-2.0)

Picture-locked Foley: the model watches the **video** and generates sound timed to on-screen action. Optional text only steers; it does not replace the picture.

## Input Asset

- [mage_crash_discovery_video.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/mage_crash_discovery_video.mp4)

---

## Node parameters (what each control does)

| Parameter | What it is | How to use it |
| --- | --- | --- |
| **video** (input) | Main input. The clip the model “hears” with its eyes. | Required. Prefer the locked cut. Silent or with audio both OK. |
| **audio** (input) | Optional separate soundtrack to preserve / align with the clip. | Wire when speech/SFX to keep is not already on the video’s own track. Leave unconnected if the video file already carries the audio you care about. |
| **model** | Engine release. | Use **`sfx-2.0`** (48 kHz). sfx-1.6 is older / different stem behavior. |
| **prompt** | Short text hint (optional). Experimental on video→SFX. | Empty first. Add **one line** only for off-screen sound or to push one layer (material, rain, forge, etc.). Soft guidance — always audition. |
| **negative_prompt** | Sounds to leave out (optional). Experimental. | Short list: `music, wind, crowd`. Good for stripping AI-video score. |
| **preserve_speech** | Keep dialogue from the source and build SFX around it. | **On (default):** keep lines, duck SFX under speech. **Off:** SFX/ambience only (VO later, or mute source intent). |
| **seed** | Reproducibility. | Same seed + same inputs ≈ similar take. Change / randomize to explore variants. |
| **audio** (output) | Generated mix (SFX ± preserved speech depending on settings). | Save / preview this as the main result. |
| **speech** (output) | Isolated speech stem when separation is available. | Use if you want dialogue on its own track; may be empty if no speech was found. |

Also typical (may be on the node or defaults): **duration** follows the clip window; **num_variants** 1–4 if exposed — generate a few and pick the best sync.

---

## Recommended workflow

1. Connect **video** (and **audio** only if needed).
2. Model = **sfx-2.0**.
3. Leave **prompt** / **negative_prompt** empty → run once.
4. Listen against picture.
5. If needed: one-line **prompt**, and/or **negative** `music, wind, crowd`.
6. Toggle **preserve_speech** for dialogue vs SFX-only.
7. Tweak **seed** or variants; save **audio** (and **speech** if useful).

---

## Prompt tips (video)

Describe **sounds**, not the plot. Keep it to one short line.

| Goal | Example prompt |
| --- | --- |
| Follow picture only | *(leave empty)* |
| Off-screen | `distant church bells, a dog barking two streets away` |
| Push one layer | `heavy rain on a tin roof, footsteps quiet underneath` |
| Material | `boots on gravel, metal settling, soft cavern wind` |
| Energy / sci-fi | `pulsing energy hum, soft electrical crackle, quiet rocky wind` |

**Negative (common):** `music, wind, crowd`  
(Drop `speech` from negative if you want dialogue kept.)

---

## With sound vs silent source

| Source | Suggestion |
| --- | --- |
| Has dialogue you want | Keep audio on the clip (or wire **audio**), **preserve_speech on** |
| Music-heavy AI clip, keep lines | preserve on + negative `music` |
| Silent / SFX-only / VO later | Silent clip OK, or **preserve_speech off** |

---

## Example (mage crash discovery ~5 s)

**First try:** empty prompt, preserve_speech as needed.

**If you want to steer the energy bed:**
```
Pulsing magenta energy hum from the crashed ship cockpit, soft electrical crackle, quiet rocky cavern wind, distant metal settling
```

**Negative:** `music, crowd, birds`

---

## Paste-ready template note

> Video drives timing. Start with an empty prompt; add one short line only for off-screen detail or to push one layer. Use negative to drop unwanted layers (`music, wind, crowd`). Keep Preserve speech on for dialogue; off for SFX-only. Prompt is soft guidance — audition variants.

</details>

<details><summary>Note: Seed</summary>

The `seed` is fixed by default. Change it if you want different output with the same prompt.

</details>
