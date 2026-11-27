# TypeSafe Jev: Gate, Score, Classify, Pick

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_typesafe_jev_decision)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_typesafe_jev_decision-1.webp" width="360" alt="TypeSafe Jev: Gate, Score, Classify, Pick api_typesafe_jev_decision-1.webp">

> Jev answers a yes/no, scored, multiple-choice or pick-from-a-batch question about text, images or both, and returns a value the graph can branch on. Four complete cases share one workflow: a publish gate on a single image, two candidates scored 1-10 against the same question and compared, free-form classification into your own option list, and picking the best image out of a batch. Copy the case you need — each is wired end to end.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_typesafe_jev_decision.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_typesafe_jev_decision.json)

## Details

| | |
|---|---|
| Name | `api_typesafe_jev_decision` |
| Category | Foundation › LLM |
| Output | llm |
| Models | TypeSafe Jev |
| Tags | API, Image, LLM |
| Type | API |
| Date | 2026-11-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 0 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | girl_red_umbrella_station.png |
| input | `LoadImage` #9 | image | cyclist_in_rain_night_street.png |
| input | `LoadImage` #16 | image | ramen_bowl_top_view.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 6 |  |
| `PreviewAny` | 6 |  |
| `MarkdownNote` | 5 |  |
| `PreviewImage` | 2 |  |
| `TypeSafeJevScore` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `ComfyMathExpression` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `ImageFromBatch` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `TypeSafeJevChoice` | 1 |  |
| `TypeSafeJevPickImage` | 1 |  |
| `TypeSafeJevYesNo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# TypeSafe Jev — four decisions in one graph

Jev answers a question about text, images or both and hands the answer back as a value the graph can branch on.
The same model is exposed four ways; every case below is wired end to end, so copy the one you need.

**Input assets (demo):**
- [cyclist_in_rain_night_street.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/cyclist_in_rain_night_street.png)
- [ramen_bowl_top_view.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ramen_bowl_top_view.png)
- [girl_red_umbrella_station.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/girl_red_umbrella_station.png)

- **Case 1 · one image, one verdict** — a yes/no question plus the probability behind it. The cheapest gate you can put in front of an expensive node.
- **Case 2 · two candidates, one winner** — score both, compare the numbers with a math rule, let a switch pass the winner downstream.
- **Case 3 · your own options** — classify into a list you write, one option per line.
- **Case 4 · pick from a batch** — pick the image that matches the prompt, then keep it with `index`.

All four cases run in one queue. These are API (partner) nodes: sign in with a Comfy account, or set an API key
(Settings → API Keys → My API Key).

## What the nodes return

| Node | Outputs |
| --- | --- |
| **TypeSafe Jev (Yes/No)** | `result` (BOOLEAN), `answer` ("yes"/"no"), `probability` (0–1) — flips at the threshold widget, 0.01–0.99 |
| **TypeSafe Jev (Choice)** | `choice` (STRING), `option_index` (INT, from 0), `confidence` (0–1) |
| **TypeSafe Jev (Pick Image)** | `index` (INT, from 0), `confidence` (0–1) |
| **TypeSafe Jev (Score)** | `result` (BOOLEAN), `score` (1–10) — true when score ≥ threshold, 1–10 |

Connect text (`text`), up to **32 images** (`image_1…image_32`), or both. Name the sockets in the question,
e.g. *"Does image_2 show the same person as image_1?"* — the model sees those names.

## How to use

1. Sign in, or paste an API key.
2. Swap the demo images in the `Load Image` nodes.
3. Ask one thing per node, and phrase it so **"yes"** — or the first option — is the case you act on.
4. Tune the threshold (0.01–0.99 for yes/no, 1–10 for score) until false positives stop hurting.
5. Route `result` into `If/Else Switch`, or `index` / `option_index` into a dispatch rule.

**Cost** is per token, so a short question and one image cost a fraction of a cent. Put the decision *before*
the expensive step and put that step on the accepted branch — the rejected branch then costs nothing.

</details>

<details><summary>MarkdownNote</summary>

### Case 1 · one image, one verdict

`Load Image → Jev (Yes/No) → Preview as Text`

*"Is there a person in the image?"* — `probability` is the confidence in "yes", `result` turns true once it
clears the threshold (0.5 here). Good for publish gates: subject facing the camera, clean background, watermark or
logo detection, content checks. Change the question, run it, watch `probability` move — then wire `result` into
a switch.

</details>

<details><summary>MarkdownNote</summary>

### Case 2 · two candidates, one winner

Each image gets its own 1–10 score against the same question; `Math Expression` compares the two floats and
`If/Else Switch` passes the winner to `Preview Image`.

Rules you can drop into the expression: `a > b` (current) · `a < b` · `a - b > 1` (only when clearly
better) · `a > 6 and a > b` (good in absolute terms *and* better). Both calls are billed — this is "best of two",
worth it when the next step is far more expensive.

</details>

<details><summary>MarkdownNote</summary>

### Case 3 · classify into your own options

`options` is one option per line (2 to 50 options, max 40 characters each); blank lines are skipped
and outer whitespace is trimmed, so `option_index` counts the parsed options, not the raw input lines. Add a catch-all such as `other` so an
input that fits nothing still lands somewhere. `choice` is the text, `option_index` its position from 0 — feed
that into a switch or a prompt selector.

Swap the list for your own taxonomy: camera angle, shot size, product category, tone of voice, moderation label.

</details>

<details><summary>MarkdownNote</summary>

### Case 4 · pick the winner from a batch

`Load Image ×2 → Batch Images → Jev (Pick Image)` — the node sees the batch, `text` carries what you asked for,
and `index` says which image won (from 0). `Get Image from Batch` takes the same batch plus that `index` (`length` 1) and
returns the picked image, so the rest of the graph works on one image instead of a batch.

2 to 32 images. Leave `text` empty to ask "which is best" instead of "which matches".

</details>
