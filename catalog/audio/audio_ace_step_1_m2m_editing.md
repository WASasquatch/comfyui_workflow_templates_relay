# ACE Step v1 M2M Editing

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_ace_step_1_m2m_editing)

[▶ audio_ace_step_1_m2m_editing-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_m2m_editing-1.mp3)

> Edit existing songs to change style and lyrics using ACE-Step v1 M2M.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_m2m_editing.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_m2m_editing.json)
- [Tutorial](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1)

## Details

| | |
|---|---|
| Name | `audio_ace_step_1_m2m_editing` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ACE-Step |
| Tags | Audio Editing, Audio |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 7.2 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 15 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #64 | audio | audio_ace_step_1_m2m_editing_input_audio.mp3 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ace_step_v1_3.5b.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/ACE-Step_ComfyUI_repackaged/resolve/main/all_in_one/ace_step_v1_3.5b.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LatentApplyOperationCFG` | 1 | comfy-core |
| `LatentOperationTonemapReinhard` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |
| `TextEncodeAceStepAudio` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `VAEEncodeAudio` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About ACE Step and Multi-language Input</summary>

[Tutorial](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1) 

### Model Download

- [Hugging Face:Comfy-Org/ACE-Step_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/ACE-Step_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/ACE-Step_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/ACE-Step_ComfyUI_repackaged)

Download the following model and save it to the **ComfyUI/models/checkpoints** folder.
[ace_step_v1_3.5b.safetensors](https://huggingface.co/Comfy-Org/ACE-Step_ComfyUI_repackaged/blob/main/all_in_one/ace_step_v1_3.5b.safetensors)


### Multilingual Support

Currently, the implementation of multi-language support for ACE-Step V1 is achieved by uniformly converting different languages into English characters. At present, in ComfyUI, we haven't implemented the step of converting multi-languages into English. This is because if we need to implement the corresponding conversion, we have to add additional core dependencies of ComfyUI, which may lead to uncertain dependency conflicts.

So, currently, if you need to input multi-language text, you have to manually convert it into English characters to complete this process. Then, at the beginning of the corresponding `lyrics`, input the abbreviation of the corresponding language code.

For example, for Chinese, use `[zh]`, for Japanese use `[ja]`, for Korean use `[ko]`, and so on. For specific language input, please check the examples in the instructions. 

For example, Chinese `[zh]`, Japanese `[ja]`, Korean `[ko]`, etc.

Example:

```
[verse]

[zh]wo3zou3guo4shen1ye4de5jie1dao4
[zh]leng3feng1chui1luan4si1nian4de5piao4liang4wai4tao4
[zh]ni3de5wei1xiao4xiang4xing1guang1hen3xuan4yao4
[zh]zhao4liang4le5wo3gu1du2de5mei3fen1mei3miao3

[chorus]

[verse]​
[ko]hamkke si-kkeuleo-un sesang-ui sodong-eul pihae​
[ko]honja ogsang-eseo dalbich-ui eolyeompus-ileul balaboda​
[ko]niga salang-eun lideum-i ganghan eum-ag gatdago malhaess-eo​
[ko]han ta han tamada ma-eum-ui ondoga eolmana heojeonhanji ijge hae

[bridge]
[es]cantar mi anhelo por ti sin ocultar
[es]como poesía y pintura, lleno de anhelo indescifrable
[es]tu sombra es tan terca como el viento, inborrable
[es]persiguiéndote en vuelo, brilla como cruzar una mar de nubes

[chorus]
[fr]que tu sois le vent qui souffle sur ma main
[fr]un contact chaud comme la douce pluie printanière
[fr]que tu sois le vent qui s'entoure de mon corps
[fr]un amour profond qui ne s'éloignera jamais

```

---

</details>
