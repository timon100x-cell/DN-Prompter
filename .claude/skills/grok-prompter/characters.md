# Stage 3: Characters

Goal: every character in the video has a fixed character block in the bible and an approved character sheet in `refs/`.

## Saved characters

Recurring characters live in `cast/<name>/character.md`, with any approved sheets beside it. The skeleton cowboy is there. When a video uses a saved character:

1. Copy the identity block into the video's bible unchanged.
2. Ask which outfit this video uses: a saved one, or a new one.
3. For a new outfit, ask the wardrobe questions below, write the outfit block, make a new sheet for it, and after approval add the outfit and its sheet to the cast folder so the next video can reuse it.

When Tim creates a new character he may want again, ask once at approval whether to save it to `cast/`.

## Questions for a new character

One round, with suggested answers that fit the world:

- Role in the video, in a few words.
- Age, build, height impression.
- Face: shape, eyes, skin, anything unusual. (For non-human characters: what the head looks like.)
- Hair or headwear.
- Wardrobe: each garment with material and color.
- One or two distinguishing marks, and on which side.
- Which emotions the close-ups need, if any.

## The character block

Write three things into the bible per character:

- **Identity block.** One sentence on body and face or head, with marks. This never changes.
- **Outfit block.** One sentence on the wardrobe for this video: garment, material, color.
- **Short anchor.** A phrase of about ten words used when the sheet is attached, naming the main garment, its color and one or two marks. Example: `the skeleton cowboy in his tattered brown leather duster and broken-brimmed hat`.

State left and right from the character's own side. Use the same nouns everywhere: if it is a "duster" once, it is never a "coat" later.

## Making the sheet: two steps

### Step 1: Source image

One full-body image, facing the camera, neutral pose, even light, plain light grey background. Template (fill from the blocks, then the look line):

```
[Identity block, phrased as: A ... stands facing the camera in a neutral pose, arms relaxed at the sides, visible from head to boots.] [Outfit block.] Soft, even studio light from the front with no hard shadows. Plain light grey background. Full-body shot at eye level, centered, with margin around the figure, everything sharp. [Look line]
```

Tim generates a few and picks exactly one. Tell him to discard the runner-up, because two near-identical masters turn into two slightly different characters.

### Step 2: Character sheet

An edit of the approved source:

```
Create a character sheet of this exact character on the same plain light grey background. Show three full-body views side by side at the same scale: front, left profile and back. Add one head-and-shoulders portrait facing the camera on the right. Keep the [marks], [headwear or hair], [main garments] identical in every view. Even studio light, thin gaps between views, no text or labels.
```

Save the approved sheet as `refs/<character>-<outfit>-sheet`.

## Rules for sheets

- Flat, even light and a plain light grey background. Dramatic light gets baked into the character and copied into every shot. No green screen, it bleeds green into scenes.
- One sheet per outfit. Mixed outfits on one sheet teach Grok that clothing is optional.
- Dark clothing gets "a thin rim of light along the edges" so it does not merge with the background.
- Glowing parts (such as the cowboy's red fissures) are described as thin and dim on the sheet, so the glow does not light the whole figure.
- Story secrets stay off the sheet. Something revealed later is added in that shot's prompt.
- An expression sheet only for characters whose close-ups need emotion: six head-and-shoulders panels on the same background, same wardrobe. A skull has no expressions, so the cowboy never needs one.

## Checklist before approving a sheet

Look at the image and check each line. Report only the failures.

- Same head or face in every view.
- Marks present, and on the correct side in each view (the profile view shows the side it should).
- Same hem length, collar, footwear and headwear in every view.
- Counts right: badges, buttons, belts, pockets, fingers.
- Nothing added: no extra jewelry, weapons, pockets or text.
- Views at the same scale, with margin, on a clean background.

Small failures: fix with an edit prompt. Wrong character: go back to the source image.
