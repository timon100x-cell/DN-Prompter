# Grok Imagine image rules

Last checked against xAI's documentation: 13 November 2026 (Imagine Image 2.0; xAI pages last updated 8 October 2026).

If this date is more than about two months old, tell Tim and offer to re-check the xAI image prompting guide before writing prompts.

Sources: xAI Image Prompting Guide, Image Generation and Multi-Image Editing pages (docs.x.ai), plus practice guides from Morphic, fal.ai, DIY AI and tetsuo. Tim's own test results in "Lessons" at the bottom outrank all of them.

## Settings (chosen in the Grok composer, never written in the prompt)

- Aspect ratio 16:9 for every image of a video, including references. One ratio per video keeps the series matched.
- Character sheets are the one exception to think about: 16:9 is fine, the sheet just needs margin around each view.
- Resolution 2K for references and approved shots.
- Never write flags such as `--ar`, `--stylize`, `--v`. They are Midjourney syntax and mean nothing to Grok.

## Sentence order for a new image

Four to six plain sentences, always in this order. With references attached, the role lines come first and do not count.

1. **Subject.** Who or what, pose or state, what supports them, the setting.
2. **Details.** Wardrobe, materials, counts, the focal point.
3. **Art direction.** Two or three named props and surfaces.
4. **Light.** Source, direction, hard or soft, and the subject clearly readable.
5. **Color.** Subject colors named against background colors.
6. **Composition.** Shot size, camera height, what the frame cuts off, what is sharp. Then the look line.

## Writing rules

- Open with the subject. A prompt that opens on mood or film stock returns a styled scene with a stand-in subject.
- Physical words, not quality words. "Heavy wool coat with a wide collar" works. "Epic, hyper-detailed, cinematic, masterpiece" does nothing useful, so leave such words out.
- Name each element and its count. "Three empty bottles", not "some bottles".
- State each texture once. Repeated texture words get painted onto the wrong surfaces.
- Say what should be in the picture. Long avoid-lists are ignored and the things they name tend to appear. Keep "no" for counts and one or two specific objects.
- Light that reads. Name the source and direction and ask for a readable subject. Words like "underexposed", "dark moody", "crushed shadows" pull the whole frame dark.
- No requested defects. Dust, scratches, lens fringing and light leaks are drawn as literal damage. Fine grain belongs in the look line only.
- One photograph, one frozen moment. No sequences, no before-and-after, no instructions to the model about what it "should" do.
- Emotion as something visible: "jaw tight, eyes narrowed", not "angry".
- Words that must appear in the image go in quotes with their position.
- Photoreal always. Tim's videos are photoreal film stills, so never drift into illustration words.

## Reference images

- Up to five images per edit. Use two or three; more than four dilutes each one.
- Give every reference a job in the first sentences: "Image 1 is the location: keep its layout, signs and lighting. Image 2 is the character sheet: use it for his skull, hat and clothing only." References without a job blend together.
- Attach the 16:9 location image first. The result takes the shape of the first image unless 16:9 is set by hand.
- Attach only what is in the shot. An attached reference tends to appear in the picture.
- When a character sheet is attached, write "one figure in one scene" in the composition sentence so Grok does not copy the sheet's panel layout.
- With a sheet attached, do not paste the full character block. Use the character's short anchor from the bible (garment, its color, one or two marks). A full description competes with the image and the two get averaged. Without a sheet attached, paste the full block.
- Always branch from the approved master reference. Never use a previous shot as the reference for the next one, because its small errors get passed on.
- If close-ups drift while wide shots hold, also attach the face close-up cropped from the sheet. For shots from behind, the sheet's back view does the work.

## Editing instead of regenerating

- Generate when there is no picture yet or the subject itself is wrong.
- Edit when subject and layout are right and one to three details need to change.
- Shape of an edit prompt: the changes first, then one sentence that keeps the rest.
  `Turn her collar up and remove the second paper cup. Keep her face, pose, the stall, the lighting and the framing exactly as they are.`
- Never open an edit with "keep everything". It barely changes the image.
- Never paste a full new prompt as an edit. It restages the scene.
- One to three changes per edit. More gives partial results; split them into two edits.
- If a fix fails, point at the exact part ("the left glove", "the sign above the door"). Repeating "more realistic" does nothing.
- A different time of day or weather for a location is an edit of the location master, not a new generation.

## Start frames for video

Tim's stills become the first frame of a Grok video clip, so every shot prompt describes a start frame:

- Choose the moment just before the action, not the middle of it. "Hand resting on the door handle", not "opening the door".
- Leave empty space where the movement will go.
- Keep the pose stable and physically plausible, with hands and feet visible when they will move.
- Avoid motion blur and frozen mid-air objects. The video model adds the motion.

## Instruments and hands

- Write every instrument with its counts: "a six-string electric guitar", "a four-string bass guitar", the drum kit piece by piece on its reference image.
- Hands on strings, sticks and microphones fail most often. Describe where each hand is, and check hands first in the result.
- State handedness in every guitar and bass shot, because Grok mirrors players.
- The full rules for band frames are in `band.md`.

## Open questions to settle in the first test session

Record the answer in "Lessons" and update the rule above.

1. How does the Grok app want references named: "Image 1" wording, or tags offered in the composer? Start with "Image 1". If the app shows tags when images are attached, switch to them.
2. Short anchor or full character block when a sheet is attached? Test the same shot both ways once and keep the winner.
3. Whole sheet as one reference, or a cropped single view? Start with the whole sheet.

## Lessons

Dated notes from Tim's real results. Newest first.

- 13 Nov 2026: an object with a strong usual material keeps it. "Carved wooden crown with flaking gold paint" came out as a metal crown twice. Lead with the unusual material and say how much of it shows ("bare grey wood across most of it, only patches of gold paint"), and fix with an edit that names the object. Update same day: the edit and a separate crown prompt also came out metal (silver, with added skulls). Describing how it was made (rough pine boards, iron nails, saw marks, end grain, brushed gold house paint) worked first time. Rule: for an object in an unusual material, describe how it was built, then keep it as a prop reference.
