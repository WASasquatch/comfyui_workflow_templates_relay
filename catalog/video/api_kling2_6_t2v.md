# Kling2.6: Storytelling Videos with Audio

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling2_6_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling2_6_t2v-1.webp" width="360" alt="Kling2.6: Storytelling Videos with Audio api_kling2_6_t2v-1.webp">

> Bring your stories to life with videos featuring synchronized dialogue, music, sound effects, and ambient audio from text prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling2_6_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling2_6_t2v.json)

## Details

| | |
|---|---|
| Name | `api_kling2_6_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling, Kling 2.6 |
| Tags | API, Audio, Text to Video, Video |
| Type | API |
| Date | 2025-12-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.5.0 |
| Usage | 27 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingTextToVideoWithAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Prompt Format</summary>

**Prompt Format** = **Scene** (Scene Description) + **Element** (Subject Description) + **Movement** (Movement Description) + **Audio**(Dialogue / Singing / Sound Effects / Pure Music) + **Other** (Style / Emotion / Camera)

💡

*   **Dialogue**: "Sentence" + Emotion + Speech Speed + Tone + Character Label
    *   **Single Character**: Specify voice attributes (e.g., **[Man speaking]**, "Sentence" + Deep + Fast).
    *   **Multiple Characters**: Use clear labels to distinguish (e.g., **[Character A, angrily]** says, "Sentence" **[Character B, calmly]** replies, "Sentence").

*   **Singing**: "Lyrics" + **Singing Style** + Accompaniment Description + Emotion
    *   **Style**: Pop, Opera, Country, etc.
    *   **Emotion/Techniques**: **High-pitched, Vibrato, Gentle singing.**

*   **Rap**: "Sentence (Rhyming)" + **Rhythm Style** + Emotion
    *   **Rhythm Style**: **Intense Boom Bap, Trap Style Beat, Fast Flow.**
    *   **Content**: "Sentence" should reflect **Rhyme and Meter.**

*   **Sound Effects**: Sound Source (Action/Object) + State + **Professional Sound Effects**
    *   **Structure**: [Object: Wooden Door] suddenly [Action: **Slams**] + [Sound Effect: **Bang**].
    *   **Material/State: Glass Breaking, Metal Impact, Screeching Brakes.**

*   **Ambient Sound**: Scene + **Sound Elements + Spatial Reverb**
    *   **Elements: Rain, Insects, Crowd Murmurs, Traffic.**
    *   **Spatial Feel: Echo in an Open Hall (Reverb), Small Room Acoustics.**

*   **Pure Music**: **Instrument Type + Music Genre** + Emotion
    *   **Structure: Piano Performance + Jazz + Melancholy.**
    *   **Genres: Classical, Rock, Electronic.**

**Tip**: It is recommended to use quotation marks " " to clarify sound content when writing prompts.

</details>
