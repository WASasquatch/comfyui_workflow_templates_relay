# Fish Audio: Voice Clone to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_fishaudio_voice_clone_tts)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_voice_clone_tts-1.webp" width="360" alt="Fish Audio: Voice Clone to Speech api_fishaudio_voice_clone_tts-1.webp">

> Clone any voice from a short recording, then use it to speak any script with Fish Audio. Record 2-3 clips of 15-20 seconds, connect them to the Instant Voice Clone node, and the cloned voice feeds straight into text to speech with no training wait. Add emotion tags to control how your cloned voice delivers each line. Great for personalized narration, character voices, and content in your own voice.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_voice_clone_tts.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_fishaudio_voice_clone_tts.json)

## Details

| | |
|---|---|
| Name | `api_fishaudio_voice_clone_tts` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Fish Audio |
| Tags | API, TTS, Voice Cloning |
| Type | API |
| Date | 2026-08-31 |
| Author | ComfyUI |
| Download size | 102.4 MB |
| Min ComfyUI version | 0.34.0 |
| Usage | 178 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #11 | audio | api_fishaudio_voice_clone_tts_fish_audio_example.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FishAudioInstantVoiceClone` | 1 |  |
| `FishAudioTextToSpeech` | 1 |  |
| `FishAudioVoiceSelector` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `RecordAudio` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Guide</summary>

## Fish Audio Text to Speech

Generate speech from text with a preset Fish Audio voice.

### How to use

1. Sign in with your ComfyUI account. API nodes are pay per use.
2. Type your script in the `text` field of the Fish Audio Text to Speech node.
3. A preset voice is already connected. To change it, pick another voice in the Voice Selector, or switch to `custom` and paste a voice model ID from fish.audio.
4. Keep parameters at their defaults unless needed.
5. Queue the prompt, then preview or save the audio.

### Inline tags

Write tags directly in the text. A tag applies from where it appears to the end of the sentence, or until the next tag.

**Emotion** (start of sentence, one per sentence):

- [happy] [sad] [angry] [excited] [calm]
- [nervous] [confident] [surprised] [scared] [worried]
- [frustrated] [empathetic] [proud] [relaxed] [curious]
- ...and more: [sarcastic] [nostalgic] [determined] [hopeful] [bored] ...

**Tone** (control volume and intensity):

- [whispering] [shouting] [screaming]
- [soft tone] [in a hurry tone] [emphasis]

**Sound effects** (add matching text after, e.g. "Ha, ha" after [laughing]):

- [laughing] [chuckling] [sobbing] [crying loudly]
- [sighing] [groaning] [panting] [gasping]
- [yawning] [snoring] [clear throat]

**Pause and background:**

- [break] [short pause] [long pause] [long-break]
- [audience laughing] [background laughter] [crowd laughing]

### Tag rules

- One main emotion per sentence, max 3 tags combined
- Pair physical tags with emotions: [whispering][scared], [panting][tired], [shouting][angry]
- Intensity modifiers: [slightly sad], [very excited], [extremely angry]
- Free-form descriptions work: [tired, end of a long shift]

### Example

[excited] Welcome back!
[chuckling] You missed a lot.
[calm] Let's get started.

### Multi-speaker

With two or more voices connected, mark speaker changes:

@Voice1 [nervous] Who's there?
@Voice2 [calm] Just me. Relax.

</details>
