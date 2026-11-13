# DN Prompter

A guided tool for writing Grok Imagine image prompts. Every video gets its own world: its own characters, locations, light and mood.

## How to use it

Open the DN Prompter project in Claude on any device and write one of these:

| You write | What happens |
| --- | --- |
| `New video: <name>` | Claude starts the world questions for a new video |
| `Continue video: <name>` | Claude reads where you left off and carries on |
| `Add a character` / `Add a location` | Claude asks a few questions and writes the reference prompts |
| Paste your shot list | Claude writes a prompt for each shot, one at a time |
| Upload a Grok result | Claude checks it against the prompt and says approved, or gives you a fix |

## The five stages

1. **World.** Short rounds of questions about place, time, light, color and camera.
2. **Look test.** Three test images. You pick one and the look is locked.
3. **Characters.** For each character: one source image, then a character sheet.
4. **Locations.** For each place: an empty master view, a reverse angle and a closer corner.
5. **Shots.** One prompt per shot from your list, with the references to attach, then check and fix.

## Where things are

- `videos/` holds one folder per video, with its bible (the world and all fixed descriptions), the prompt log and the approved reference images.
- `cast/` holds characters you reuse, such as the skeleton cowboy and his outfits.
- `.claude/skills/grok-prompter/` holds the method and the Grok rules. `grok-rules.md` in that folder is the one place the Grok rules live, including lessons from your own results.

## In Grok Imagine

- Set 16:9 and 2K in the composer for every image.
- Attach references in the order Claude gives.
- Paste the prompt exactly as given.
