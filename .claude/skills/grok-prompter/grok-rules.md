# Grok Imagine image rules

Last checked against xAI's documentation: 13 November 2026 (Imagine Image 2.0; xAI pages last updated 8 October 2026).

If this date is more than about two months old, tell Tim and offer to re-check the xAI image prompting guide before writing prompts.

Sources: xAI Image Prompting Guide, Image Generation and Multi-Image Editing pages (docs.x.ai), plus practice guides from Morphic, fal.ai, DIY AI and tetsuo. Tim's own test results in "Lessons" at the bottom outrank all of them.

## Settings (chosen in the Grok composer, never written in the prompt)

- Aspect ratio 16:9 for every image of a video, including references. One ratio per video keeps the series matched.
- Character sheets are the one exception to think about: 16:9 is fine, the sheet just needs margin around each view.
- Resolution 2K for references and approved shots.
- Never write flags such as `--ar`, `--stylize`, `--v`. They are Midjourney syntax and mean nothing to Grok.
- **A new Grok chat for every new image or step.** In an existing chat Grok builds on its own last result instead of the attached images (King of Nothing, 16 Nov 2026). Only an edit of the image just made stays in the same chat. Say "New chat" in the settings line of every prompt that needs one.

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
- **Skeleton skulls are smooth and intact.** Write "smooth, intact skull" (or "smooth, clean skull") in every prompt or edit where a skull is in frame, including short focus edits. Never write cracks, fissures, seams, glowing marks or anything similar on the skeleton cowboy, in any video (Tim, 13 Nov 2026). Grok adds hairline cracks and seams on its own in close-ups, so check for them every time. Band members may get soot and ash when the story burns, but no cracks.

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

## Putting a character in a location

Tested 16 Nov 2026 (King of Nothing shot 5). Writing one prompt that sets a new camera angle, places a character and lights him at the same time fails: Grok rebuilds the building, keeps the sheet's studio light and makes the person too big. Split the work:

1. **Empty plate first.** Make the location from the exact camera position of the shot, with nobody in it (an edit of the master that moves the camera, see `locations.md`). Approve it on its own. One plate can serve several shots.
2. **Add the character as an edit of the plate.** Attach the plate first, the sheet second. Open with "Add [anchor] from Image 2 to Image 1", say where he stands and what he does, and end with "Keep [the landmarks], the camera position and the framing of Image 1 exactly as they are."
3. **Size against something in the plate:** "He is half as tall as the gate doors, and his hat reaches the lower edge of the hatch."
4. **Light from the plate, not the sheet:** "Use Image 2 only for his face, hat and clothing, not its light or pose. Light him with the [light] already in Image 1, with a soft shadow on the ground under his feet."
5. **If he still looks pasted on:** one edit that relights only him ("Match the light on the merchant to the grey daylight on the wall, and add a soft contact shadow under his shoes. Keep everything else exactly as it is.").
6. **Openings keep their size only if you say so.** In shot 7 a small hatch "slid open" grew into a big window. Write "the hatch opens, the same size as in Image 1".
7. **Closer shots** of the same moment are short focus edits of the approved wider shot, as with the band.

Tim works in a fresh Grok chat for each step, so Grok starts from the attached images and not from its own last result.

## Start frames for video

Tim's stills become the first frame of a Grok video clip, so every shot prompt describes a start frame:

- Choose the moment just before the action, not the middle of it. "Hand resting on the door handle", not "opening the door".
- Leave empty space where the movement will go.
- Keep the pose stable and physically plausible, with hands and feet visible when they will move.
- Avoid motion blur and frozen mid-air objects. The video model adds the motion.

## Video prompts

Tim animates every approved start frame in Grok video and wants a short video prompt with each shot (decided 19 Nov 2026). Hand it over below the image prompt, in its own code block, labelled "Video:".

- **Only what moves.** The start frame already sets the place, people, light and look. Do not describe them again.
- **Two or three short sentences:** what the subject does, what moves in the scene (fog, smoke, flames, candles, dust), and one camera move ("The camera pushes in slowly", "holds still", "slides sideways"). One camera move per clip.
- **Sized to the clip.** Write for the clip length in the song map (usually 4 to 5 seconds), so one action, not a sequence.
- **Skeletons move little.** A moving skull tends to grow cracks and extra details, so the king stays still or makes one slow movement; his menace comes from stillness. Band players can play with energy, since their skulls are often small in frame or soft.
- **Lighting changes are allowed** when the start frame prepares them (a faint glow that grows as torches come closer).
- **No new subjects appearing out of nothing.** If something must appear (a skull in a hatch), it should already be in the start frame, or Grok invents it and it will not match the sheet.

### Lip-sync

For a singing shot, write a longer prompt (5 to 8 sentences): the start frame, the exact words in quotes, how long they take ("from 'The' to 'eyes' over the full 10 seconds"), how the jaw moves on the long vowels, the delivery (theatrical, dramatic, with bravura), and what the band and room do around him. Tell Tim to set the clip length to match the line. Grok cannot hear the song, so the mouth only roughly follows the words; long open vowels make it easier to line up in the edit. For another tool (for example Suno video), ask whether it has a separate lyrics field and keep the words there if it does.

## Instruments and hands

- Write every instrument with its counts: "a six-string electric guitar", "a four-string bass guitar", the drum kit piece by piece on its reference image.
- Hands on strings, sticks and microphones fail most often. Describe where each hand is, and check hands first in the result.
- State handedness in every guitar and bass shot, because Grok mirrors players.
- The full rules for band frames are in `band.md`.

## Open questions to settle in the first test session

Record the answer in "Lessons" and update the rule above.

1. Settled (King of Nothing, Nov 2026): "Image 1", "Image 2" wording in the order of attachment works.
2. Short anchor or full character block when a sheet is attached? Test the same shot both ways once and keep the winner.
3. Whole sheet as one reference, or a cropped single view? Start with the whole sheet.

## Lessons

Dated notes from Tim's real results. Newest first.

- 27 Nov 2026 (Hide): Tim chose to describe the cowboy fully in text in every prompt and not attach his sheet, so the character takes the scene's light instead of the sheet's studio light. When Tim asks for this, write a detailed description from the approved sheet (every garment, its shape, color and details, hands, skull) into the bible and paste it word for word; the sheet stays as the check reference. Watch whether details drift between shots and record the result here.

- 17 Nov 2026 (burned castle): the ruin built detail-first drifted. The throne grew as tall as the towers, too much of the building stayed standing, and burned spikes filled the horizon like a burned forest. Tim asked for "a total view of the castle burned down" first. Rule: make the overview of each story state first and build every detail shot of that state from it (see `locations.md`). Name the background that must stay ("the open meadow beyond, unburnt") and give big props a size against the building.
- 16 Nov 2026 (intro I1): a landmark left out of the prompt is left out of the image. The bridge vanished because the prompt did not name it. Every prompt of a location names its "must stay" landmarks from the bible, even when the location image is attached.
- 16 Nov 2026 (crown close-up): a close-up of the king's skull came back with hairline cracks and a seam that no prompt asked for, and it was lit like a studio while the wide shot was candlelit. A focus edit of a lit scene needs the light named again ("lit only by the candles, as in Image 2") and "smooth, intact skull".

- 13 Nov 2026 (Tim's taste): in shots that feature one person, he likes the background softly out of focus with the scene still populated, rather than everything sharp or an empty room. Add "the background softly out of focus" to the composition sentence; the look line stays as it is.
- 13 Nov 2026 (band master): a line-up reference passes on its arrangement and flat studio light. Say it is for clothing only, "not their poses or arrangement", stagger the figures in depth, and ask for light falloff and floor shadows. Fixed the "looks fake" result on the next try; band.md's template now does this.
- 13 Nov 2026 (band, King of Nothing): editing one member out of a five-person line-up into a sheet works without cropping; all five came back as single-member sheets. Watch for bleed between neighbours: the guitarist's profile view wore the banjo player's jacket. A bare skull tends to get seam lines and spots; say "smooth, clean skull" again in the sheet prompt.
- 13 Nov 2026: an object with a strong usual material keeps it. "Carved wooden crown with flaking gold paint" came out as a metal crown twice. Lead with the unusual material and say how much of it shows ("bare grey wood across most of it, only patches of gold paint"), and fix with an edit that names the object. Update same day: the edit and a separate crown prompt also came out metal (silver, with added skulls). Describing how it was made (rough pine boards, iron nails, saw marks, end grain, brushed gold house paint) worked first time. Rule: for an object in an unusual material, describe how it was built, then keep it as a prop reference.
- Closer views of a location (16 Nov 2026, King of Nothing): "show a closer view of the gate" made Grok invent a new building (square towers, giant gate, moat against the wall). Write it as the camera moving forward to a named spot, and list the features of the master that must stay (tower shape, roofs, window count, how big the door is next to a person).
- Sheets carry studio light and scale into shots (16 Nov 2026, King of Nothing shot 5): the merchant came out too big for the gate, bright and evenly lit, pasted on. In every shot with a sheet attached, give a scale anchor against the location ("the gate is about twice his height") and a light-match sentence: "He is lit by the same [light] as the [location], with no studio light, his colors slightly muted by the [weather], and a soft shadow on the ground at his feet."
