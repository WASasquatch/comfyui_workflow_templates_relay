# Single Image to Multiple Consistent Shots

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-multiple_consistent_shots-nb_pro)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-multiple_consistent_shots-nb_pro-1.webp" width="360" alt="Single Image to Multiple Consistent Shots templates-multiple_consistent_shots-nb_pro-1.webp">

> Upload an input image and automatically generate X prompts for camera angle and shot type.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-multiple_consistent_shots-nb_pro.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-multiple_consistent_shots-nb_pro.json)

## Details

| | |
|---|---|
| Name | `templates-multiple_consistent_shots-nb_pro` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Nano Banana Pro |
| Tags | API, Image Edit, Character Reference |
| Type | API |
| Date | 2026-01-26 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 38 |
| Nodes | 94 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | sportbike_rider.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Batch Prompt Iterator** (8 nodes)
- **New Subgraph** (3 nodes)
- **New Subgraph** (5 nodes)
- **Batch Prompt Iterator** (8 nodes)
- **New Subgraph** (5 nodes)
- **Batch Prompt Iterator** (8 nodes)
- **New Subgraph** (3 nodes)
- **New Subgraph** (5 nodes)
- **New Subgraph** (4 nodes)
- **Batch Prompt Iterator** (8 nodes)
- **Batch Prompt Iterator** (8 nodes)
- **Batch Prompt Iterator** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 13 | comfy-core |
| `Reroute` | 11 |  |
| `PreviewImage` | 7 | comfy-core |
| `BatchImagesNode` | 6 | comfy-core |
| `GeminiImage2Node` | 6 | comfy-core |
| `MarkdownNote` | 6 |  |
| `PrimitiveInt` | 6 | comfy-core |
| `PrimitiveStringMultiline` | 6 | comfy-core |
| `RegexExtract` | 6 | comfy-core |
| `RegexReplace` | 6 | comfy-core |
| `SaveImage` | 6 | comfy-core |
| `SimpleMath+` | 6 | comfyui_essentials |
| `SomethingToString` | 6 | comfyui-kjnodes |
| `GeminiNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>

<details><summary>MarkdownNote</summary>

# Prompt Selector Regex Pattern

## Pattern
(?:^(?!\s*\*?\s*$).+$\n(?:^\s*\*?\s*$\n)*){0}^(?!\s*\*?\s*$)(.+)$

## Settings
- mode: "First Group"
- multiline: true
- dotall: false
- group_index: 1

## How it works

| Part                      | Meaning                                         |
|---------------------------|-------------------------------------------------|
| (?!\s*\*?\s*$)            | Lookahead: line is NOT blank or just *          |
| ^(?!\s*\*?\s*$).+$        | Match a content line                            |
| \n                        | Newline after content                           |
| (?:^\s*\*?\s*$\n)*        | Consume zero or more separator lines (blank/*)  |
| {0}                       | Skip n blocks (replaceable index)               |
| ^(?!\s*\*?\s*$)(.+)$      | Capture the target prompt                       |

## Index Replacement
Use Regex Replace with pattern: (?<=\{)\d+(?=\})

## Supported Formats

**Newline only:**

test1
test2
test3

**Blank lines:**

test1


test2


test3


**Asterisk separator:**

test1
*
test2
*
test3

**Asterisk with blanks:**

test1

*

test2

*

test3

</details>
