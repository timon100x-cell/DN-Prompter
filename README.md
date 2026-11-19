# DN Prompter

A guided tool for writing Grok Imagine image prompts. Every video gets its own world: its own characters, locations, light and mood.

## How to use it

Open the DN Prompter project in Claude on any device and write one of these:

| You write | What happens |
| --- | --- |
| `New video: <name>` | Claude starts the world questions for a new video |
| `Continue video: <name>` | Claude reads where you left off and carries on |
| `Add a character` / `Add a location` | Claude asks a few questions and writes the reference prompts |
| `Add the band` | Claude asks who is in the band for this video and sets up the band frames |
| Paste the lyrics with timestamps | Claude maps the song and plans each section with you before any prompts |
| Paste your shot list | Claude fits it to the song and writes an image prompt and a video prompt for each shot |
| `Where is <image>?` | Claude links the video's gallery page with every approved image |
| Upload a Grok result | Claude checks it against the prompt and says approved, or gives you a fix |

## The stages

1. **World.** Short rounds of questions about place, time, light, color and camera.
2. **Look test.** Three test images. You pick one and the look is locked.
3. **Characters.** For each character: one source image, then a character sheet.
4. **Locations.** For each place: an empty master view and the camera angles you'll need, plus one overview of each state the place goes through (night, burning, ruin).
5. **Band (optional).** A few questions about this video's skeleton band, then a line-up, the instruments and the stage in one of your locations.
6. **Song map.** Lyrics and timestamps in, a shot plan per section out. You approve each plan; no scene is used twice.
7. **Shots.** An image prompt and a video prompt per shot, with the references to attach, then check and fix.

## Where things are

- `videos/` holds one folder per video, with its bible (the world and all fixed descriptions), the prompt log and the approved reference images.
- `cast/` holds characters you reuse, such as the skeleton cowboy and his outfits.
- `.claude/skills/grok-prompter/` holds the method and the Grok rules. `grok-rules.md` in that folder is the one place the Grok rules live, including lessons from your own results.

## In Grok Imagine

- Set 16:9 and 2K in the composer for every image.
- Attach references in the order Claude gives.
- Paste the prompt exactly as given.
- Start a new Grok chat whenever the prompt says "New chat".
