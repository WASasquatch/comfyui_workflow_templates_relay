# HeyGen Decision 1: Gate and Pick

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_decision_1)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_decision_1-1.webp" width="360" alt="HeyGen Decision 1: Gate and Pick api_heygen_decision_1-1.webp">

> Ask HeyGen Decision 1 a yes/no or scored question about text, images, audio or video, then route the graph on the answer. Two patterns share one workflow: a single image gated by a yes/no verdict, and two images scored 1-10 and compared so a switch passes the better one downstream. Use it as a cheap quality gate in front of expensive generation, or to pick the best of several candidates.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_decision_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_decision_1.json)

## Details

| | |
|---|---|
| Name | `api_heygen_decision_1` |
| Category | Foundation › LLM |
| Output | llm |
| Models | HeyGen Decision 1 |
| Tags | API, Image, LLM |
| Type | API |
| Date | 2026-11-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.0 |
| Usage | 25 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | cartoon_kid_inventor.png |
| input | `LoadImage` #4 | image | tiefling_sorcerer.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 7 |  |
| `MarkdownNote` | 3 |  |
| `HeyGenDecisionScore` | 2 |  |
| `LoadImage` | 2 |  |
| `ComfyMathExpression` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `HeyGenDecisionYesNo` | 1 |  |
| `PreviewImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

### Case 1 · one image, one verdict

`Load Image → Decision (Yes/No) → Preview as Text`

The question is *"Is there a person in the image?"*. `probability` is the confidence in "yes"; `result`
turns true once it clears the threshold (0.5 here).

Good for publish-ready checks, subject facing the camera, clean background, watermark / logo detection,
content gates. Change the question, run it, watch `probability` move — then wire `result` into a switch.

</details>

<details><summary>MarkdownNote</summary>

### Case 2 · two images, scored and compared

Each image gets its own 1–10 score against the same question; `Comfy Math Expression` compares the two floats
and `If/Else Switch` passes the winner to `Preview Image`.

Rules you can drop into the expression: `a > b` (current) · `a < b` · `abs(a - b) > 1` (only when clearly
better) · `a > 6 && a > b` (good in absolute terms *and* better). Both calls are billed — this is "best of two",
worth it when the next step is far more expensive.

</details>

<details><summary>MarkdownNote</summary>

# HeyGen Decision — two cases

The same partner node used two ways in one graph.

- **Case 1 · one image, one verdict** — ask a yes/no question, read the boolean and the probability. The cheapest gate you can put in front of an expensive node.
- **Case 2 · two images, scored and compared** — score both candidates, compare the numbers with a math rule, and let a switch pass the winner downstream.

Both cases run in one queue. These are API (partner) nodes: sign in with a Comfy account, or set an API key
(Settings → API Keys → My API Key).

## What the nodes return

| Node | Outputs |
| --- | --- |
| **HeyGen Decision (Yes/No)** | `result` (BOOLEAN), `answer` ("yes"/"no"), `probability` (0–1) — flips at the threshold widget, 0.01–0.99 |
| **HeyGen Decision (Score)** | `result` (BOOLEAN), `score` (1–10) — true when score ≥ threshold, 1–10 |

Connect text (optional), up to **4 images** (`image_1…image_4`), one **audio** (`audio_1`) or one **video**
(`video_1`, ≤60 s). Name them in the question, e.g. *"Does image_2 show the same person as image_1?"*

## How to use

1. Sign in, or paste an API key.
2. Swap the demo images in the two `Load Image` nodes.
3. Ask one thing per node, and phrase it so **"yes" is the case you act on**.
4. Tune the threshold — raise it when a false positive is expensive.
5. Route `result` into `If/Else Switch` (two branches) or into `Comfy Math Expression` + switch (a rule).

**Cost** is per input token, so a short question or one image costs a fraction of a cent. Put the decision
*before* the expensive step and put that step on the accepted branch — the rejected branch then costs nothing.

</details>
