# Kling2.6: Animate Images with Audio

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling2_6_i2v-1.webp" width="360" alt="Kling2.6: Animate Images with Audio api_kling2_6_i2v-1.webp">

> Transform static images into dynamic videos with synchronized dialogue, singing, sound effects, and ambient audio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling2_6_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling2_6_i2v.json)

## Details

| | |
|---|---|
| Name | `api_kling2_6_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling 2.6, Kling |
| Tags | Image to Video, Video, API, Audio |
| Type | API |
| Date | 2025-12-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.5.0 |
| Usage | 14 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | lizard_rapper_in_bar.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingImageToVideoWithAudio` | 1 |  |
| `LoadImage` | 1 |  |
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
