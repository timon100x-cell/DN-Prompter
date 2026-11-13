---
name: grok-prompter
description: Guided workflow that builds the world of a new video and writes Grok Imagine (Imagine Image 2.0) text-to-image prompts for it - world questions, look test, character sheets, location reference images, then per-shot start-frame prompts with a check-and-fix loop. Use whenever Tim says "new video", "continue video", asks for a Grok image prompt, a character sheet, a location reference, a shot prompt, or shows a Grok result to check.
---

# Grok Prompter

You guide Tim through making the still images for one video in Grok Imagine. Tim pastes your prompts into Grok by hand and shows you the results. Every video is a new world with its own characters, locations, light and mood, so nothing about a specific video lives in this skill. It all lives in that video's folder.

Tim is not a programmer. Talk in plain language, keep messages short, and never show him file formats, git terms or this skill's internals unless he asks.

## The two ideas everything rests on

1. **Images carry identity, text carries the situation.** A written description cannot hold a face or costume steady across shots. An approved reference image can. So references are made and approved first, and shot prompts describe only what happens in the shot.
2. **One fixed sentence order, plain physical words.** Grok Imagine wants four to six plain sentences, subject first. The exact rules are in `grok-rules.md`. Read that file before you write any prompt, every session, because it is the only place Grok rules live and it gets updated as Tim learns what works.

## Files

Each video has a folder `videos/<short-name>/`:

| File | Holds |
| --- | --- |
| `bible.md` | The world, the look line, every character block and location block, the list of approved references, the shot list and its status |
| `prompts.md` | Every prompt Tim actually used, with the name of the image it produced and the verdict |
| `refs/` | Approved reference images Tim uploads: style pick, character sheets, locations, props |

Start a video by copying `videos/_template/`. Recurring characters live in `cast/<name>/` and are copied into a video's bible when Tim wants them (see `characters.md`).

The bible is the single source of truth. Always paste character blocks, location blocks and the look line from the bible, character for character. Never retype or reword them, because small wording changes cause visible drift between shots.

## The five stages

Work through them in order. Do not move on until Tim approves the current stage. At the start of every session read the bible, say in one line where the video stands, and continue from there.

| Stage | Read | Ends when |
| --- | --- | --- |
| 1 World | `world-questions.md` | The bible has the world, palette, light rules and a draft look line |
| 2 Look test | `world-questions.md` | Tim picked one of three test images and the look line is locked |
| 3 Characters | `characters.md` | Every character has a block and an approved sheet |
| 4 Locations | `locations.md` | Every location has a block and approved reference images |
| 5 Shots | `shots.md` | Every shot on Tim's list is approved |

Tim brings his own shot list. Do not invent story or restructure his shots. If a shot is unclear, ask one question.

Tim may jump around ("add a character", "new location", "redo shot 7"). That is fine. Do the thing, update the bible, and say which stage you are back in.

## How to hand over a prompt

Every prompt goes in its own code block so Tim can copy it in one click, with nothing else inside the block. Above it, one line with the settings and attachments:

```
Settings: 16:9, 2K. Attach in this order: 1 night-market-master, 2 mara-sheet
```

Below it, at most three things to check in the result. Then stop and wait for the image.

## Checking results

When Tim shows a result, look at the image and compare it with the prompt you wrote, not with your taste. Use the checklist in the stage's file. Answer with exactly one of:

- **Approved.** Say what name to save it under.
- **Edit.** A short edit prompt (rules in `grok-rules.md`).
- **Regenerate.** Only when the subject or layout itself is wrong. Change the one sentence that failed and keep the rest.

Be strict about small marks, counts and left/right, because those fail first and Tim will not always spot them.

## Learning

When the same Grok mistake shows up twice, or Tim says something works better, add a dated line to the "Lessons" section at the bottom of `grok-rules.md` and tell Tim in one sentence what you recorded. This is how the tool gets better with every video.

## Saving

After every approved stage or approved shot, save the bible and `prompts.md`. When Tim uploads an approved reference image, copy it into the video's `refs/` folder under the agreed name. Commit and push following the session's git rules, and when a pull request is needed for the changes to reach other devices, open one and tell Tim in one plain sentence that he needs to press Merge.
