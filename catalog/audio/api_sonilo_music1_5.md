# Sonilo Music 1.5: Lyrics to Song

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_sonilo_music1_5)

[▶ api_sonilo_music1_5-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_music1_5-1.mp3) <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_music1_5-1.webp" width="360" alt="Sonilo Music 1.5: Lyrics to Song api_sonilo_music1_5-1.webp">

> Turn your own words into a finished song with Sonilo Music 1.5: describe the style and the scene, then add a Lyrics: block with [Verse] and [Chorus] tags and the model sings it over full instrumentation. Auto length follows the lyrics, or set the duration yourself.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_music1_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_sonilo_music1_5.json)

## Details

| | |
|---|---|
| Name | `api_sonilo_music1_5` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Sonilo |
| Tags | API, Audio, Music, Text to Music |
| Type | API |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.0 |
| Usage | 66 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `SoniloMusic15` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Sonilo Music 1.5

**One prompt, one song.** Describe the music, then write the words: the model sings the `Lyrics:` block you give it, or writes its own if you leave that block out.

---

### What this graph does

1. **Sonilo Music 1.5**: turns a single text prompt into a song with sung vocals.
2. **Duration**: `auto` picks a length from the prompt, or set the seconds yourself.
3. **Save Audio (Advanced)**: writes the track as an MP3 you can play from the node.

---

### Writing the prompt

Two parts, in this order: the musical direction first, the lyrics after it.

| Part | What goes in it |
|------|-----------------|
| **Direction** | Genre, tempo, mood, instruments, vocal type, how long the track should feel, and where it will be used |
| **Lyrics** | The line `Lyrics:` on its own line, then the song underneath |

```
Warm indie folk at 104 BPM, fingerpicked guitar, brushed drums, upright bass,
male vocal with light harmonies, written for a cooking video intro.

Lyrics:
[Verse]
Flour on the wooden board
Make a well right in the core

[Chorus]
Roll it out, roll it thin
Let the kitchen groove begin
```

Without a `Lyrics:` block the model writes its own words from the direction alone, which is the faster way to sketch a style. For a music bed instead of a song, say so in the direction: `instrumental`, `no vocals` or `lyric-free`.

### Section tags

Put a bracketed tag on its own line above the section it covers. `[Verse]`, `[Chorus]` and `[Bridge]` cover most songs; write the tag again with its lines every time that section comes back, so a song with three choruses carries `[Chorus]` three times.

Keep the prompt at 2000 characters or less for direction and lyrics together: a six-section song usually lands around 1000 to 1300 characters, including the direction.

### Duration

- **auto**: the song is sized to the lyrics you wrote. The example above, six sections at roughly 1100 characters of lyrics, came back as a 2:30 track.
- **custom** with `seconds` (10 to 360): forces a fixed length instead. Lyrics that do not fit are cut, lyrics that are too short are repeated.

### Seed

Seed only decides whether the node runs again. It does not make the result repeatable: the same prompt and seed return a different song each run, so re-run to collect variations.

</details>
