# DN Prompter

This repository is Tim's tool for writing Grok Imagine image prompts, one new world per video. It is a set of instructions for Claude, not a program.

- The tool is the skill in `.claude/skills/grok-prompter/`. Use it whenever Tim says "new video", "continue video", asks for a Grok image prompt, a character sheet, a location reference or a shot prompt, or shows a Grok result.
- Each video lives in `videos/<short-name>/` (copy `videos/_template/` to start one). Its `bible.md` is the single source of truth for that video.
- Recurring characters live in `cast/`.
- Most videos also have frames of a skeleton metal band playing in one of the story's locations. The band is different every video and is never the skeleton cowboy. See `band.md` in the skill.
- All Grok rules live in one file: `.claude/skills/grok-prompter/grok-rules.md`. Change rules there and nowhere else.

Tim is not a programmer and works on Windows. Use plain language, keep replies short, and do not show git or file details unless he asks. He pastes prompts into Grok by hand and writes his own shot lists. All images are photoreal film stills at 16:9 and serve as start frames for Grok video.

Stay on image prompting. Do not expand into story writing, video motion prompts or editing advice unless Tim asks.
