# Stage 4B: The band (optional)

Goal: approved references for the band and its stage, and an approved still for every band shot.

Most of Tim's videos cut between the story and frames of a heavy metal band playing, preferably in one of the story's own locations. The band frames must look like they were shot in the same world on the same day as the story frames: same look line, same location references, same light.

Fixed facts (Tim, 13 November 2026):

- Every band member is a skeleton.
- The band dresses to fit the video's world.
- The skeleton cowboy is not in the band. Never put him in a band frame unless Tim asks.
- The line-up is different in every video. Nothing about the band is saved between videos, so ask the band questions fresh every time. If Tim says "same band as <earlier video>", copy that video's band section and sheets and only ask what changes.

Run this stage after the locations are approved, because the band plays in one of them. Skip it when Tim says the video has no band.

## Band questions

One round. Mark one suggested answer per question as "(a, recommended)" so a plain "yes" is clear. Suggest answers that fit this video's world.

1. **Line-up.** How many members, and who plays what? (For example: singer, two guitarists, bassist, drummer.)
2. **Wardrobe.** What does the band wear in this world? Offer two or three directions drawn from the world and the story characters' wardrobe.
3. **Instruments.** Modern metal instruments as they are, or built to fit the world (for example weathered wood and iron)? Any signature shapes or colors?
4. **Gear on stage.** Amps, cables and microphone stands visible, or instruments and drum kit only?
5. **Stage.** Which approved location do they play in, and in which light variant?
6. **Anything else in frame.** An audience, fire, story characters? Default: the band alone.

Guitarists and bassist are right-handed unless Tim says otherwise.

## Telling skeletons apart

Skeletons have no faces, so members are told apart only by what is on and around the bones. Give each member one strong difference in each of these, and never reuse one between members:

- headwear or hair (a hood, a helmet, long grey hair, a bare skull)
- the silhouette of the main garment (long coat, bare ribs with a vest, cloak, armor)
- one color accent from the video's palette
- build (tall and narrow, broad, short)

Their instrument does the rest. Propose these differences yourself in the summary after the questions and let Tim adjust.

## What goes into the bible

- **Band identity line**, shared by every member, word for word: `a skeleton with a smooth, intact, weathered bone-white skull and empty dark eye sockets`. No cracks, fissures or markings on any skull unless Tim asks.
- Per member: a **member block** (build, headwear, garments with material and color), the **instrument**, **handedness**, **stage position** (left, center, right, back) and a **short anchor** of about ten words.
- Per instrument: an **instrument block** with counts. Use these numbers unless Tim's instrument differs:
  - Electric guitar: six strings, six tuning pegs, one neck.
  - Bass guitar: four strings, four tuning pegs, a longer neck.
  - Drum kit: one bass drum, one snare drum, two rack toms, one floor tom, one hi-hat, two crash cymbals, one ride cymbal, one stool.
- **Stage:** the location, the light variant, and where the gear stands.

## References, in this order

Every reference prompt follows `grok-rules.md` and ends with the video's look line.

### 1. Line-up

One new image of the whole band standing side by side on the plain light grey background, even light, no instruments, full body, same scale. This is approved first because it shows whether the members are different enough from each other, and it lets the whole band count as one reference later.

```
[Number] skeletons stand side by side facing the camera in neutral poses, arms relaxed at their sides, each visible from skull to boots. Each has a smooth, intact, weathered bone-white skull and empty dark eye sockets. From left to right: [member 1 block]; [member 2 block]; [member 3 block]; ... Soft, even studio light from the front with no hard shadows. Plain light grey background. Wide full-body shot at eye level, all [number] figures at the same scale with clear gaps between them, everything sharp. [Look line]
```

List the members left to right in their stage order, drummer last. More than five members: make two line-ups.

### 2. Member sheets

One sheet per member who gets shots of their own, made as an edit of the approved line-up:

```
Create a character sheet of only the [second] figure from the left, alone, on the same plain light grey background. Show three full-body views side by side at the same scale: front, left profile and back. Add one head-and-shoulders portrait facing the camera on the right. Keep the skull, [headwear], [main garments] identical in every view. Even studio light, thin gaps between views, no text or labels.
```

If Grok cannot isolate one figure, ask Tim to crop that member out of the line-up and use the crop as the source for the sheet. Check each sheet with the checklist in `characters.md`.

### 3. Instruments

One clean image per different instrument, alone on the plain light grey background, whole instrument in frame, counts stated. The drum kit is one image. For instruments built in an unusual material, describe how they were built (see Lessons in `grok-rules.md`).

### 4. Stage plate

An edit of the chosen location reference: the same place with the gear set up and no people. It fixes where everything stands for every band frame.

```
Add a band's gear to this place, with no people: [the drum kit centered at the back on the floor], [one amplifier at the left and one at the right], [one microphone stand at the front center]. Keep the layout, landmarks, surfaces, lighting and framing exactly as they are.
```

Attach the drum kit image as Image 2 when the kit matters, with the job line "Image 2 is the drum kit: keep its drums and cymbals".

### 5. Band master wide

The full band in position. This is the hardest image of the video, so it is made and approved once, and other full-band angles are edits of it.

Never ask for the members to stand "in position" facing the camera: with the line-up attached, Grok copies its straight row and flat light and the band looks pasted in (King of Nothing, 13 November 2026). Stagger the depths, turn members toward each other, and ask for light falloff and floor shadows.

```
Settings: 16:9, 2K. Attach in this order: 1 stage plate, 2 line-up

Image 1 is the stage: keep its room, gear positions and lighting. Image 2 is the band line-up: use it for each member's skull, headwear and clothing only, not their poses or arrangement. [Number] skeleton musicians are spread across the stage at different depths in the quiet second before the first note: [singer anchor] at the microphone stand in the foreground center, gripping it with one hand; [guitarist anchor] further back at the left with his weight on one leg, [guitar block] low on its strap; [bassist anchor] at the right, half turned toward the drummer, holding [bass block]; and [drummer anchor] seated on the stool behind the drum kit at the back with both sticks raised. [Handedness sentence.] [Light from the location's approved variant, falling off toward the walls, each figure casting a soft shadow on the floor, every member still readable.] [Colors.] Wide shot from slightly off center at chest height, the singer large in the foreground and the band receding behind him, [number] figures in one scene. [Look line]
```

Save as `refs/band-lineup`, `refs/band-<member>-sheet`, `refs/prop-<instrument>`, `refs/stage-plate`, `refs/band-master`.

## Band shots

Band shots get their own list in the bible, numbered B1, B2 and so on, so they never mix with Tim's story shots. Tim can write his own band shots or pick from this kit. Offer the kit once, as a list he can answer with numbers.

| Kit shot | Attach | Note |
| --- | --- | --- |
| Full band, wide | stage plate, line-up | This is the band master |
| Full band, low angle or from the side | band master | An edit: "Lower the camera to knee height ..." |
| Singer, medium | stage plate, singer sheet | Hand on the microphone, jaw slightly open |
| Singer, close-up | singer sheet, stage plate | Skull and microphone, background soft |
| Guitarist, medium | stage plate, guitarist sheet, guitar | Pick resting on the strings |
| Fretting hand, extreme close-up | guitar, guitarist sheet | Bone fingers on the neck |
| Bassist, medium | stage plate, bassist sheet, bass | |
| Drummer from the front | stage plate, drummer sheet, drum kit | Both sticks raised |
| Sticks and cymbal, extreme close-up | drum kit, drummer sheet | One stick just above the cymbal |
| Over a shoulder into the room | stage plate, one member sheet | Shows the place from the stage |

Single-member shots are the reliable ones. Keep full-band shots to a few. In the kit table, "stage plate" for a single-member shot means the band master once it is approved (see the rule on focus below).

Build each band shot as in `shots.md`, with these additions:

- **The moment before the hit.** Stick raised, pick resting on the strings, jaw just opening at the microphone. The video model adds the motion.
- **Counts in the prompt.** Write the instrument with its numbers every time: "a six-string electric guitar", "a four-string bass guitar".
- **Handedness.** Right-handed means the right hand is at the strings near the body and the left hand is on the neck. Say it in the prompt for every guitar and bass shot.
- **The drummer sits.** "Seated on the stool behind the drum kit". A standing drummer is a failure.
- **Straps and cables once.** One guitar strap over the shoulder. Name a cable only if the stage plate shows amplifiers.
- **Same light as the story.** Use the light of the approved location variant, word for word from the bible.
- **One member in focus, the band still there.** Tim prefers single-member shots with the rest of the band still in their places behind, softly out of focus (13 November 2026). Attach the band master instead of the stage plate as Image 1, and write: "[member] in sharp focus, the other members in their places behind him softly out of focus." Use "one figure in one scene" only when Tim asks for a member alone.

Single-member template:

```
Image 1 is the stage: keep its layout, gear positions and lighting. Image 2 is the character sheet: use it for the skull, [headwear] and clothing only. Image 3 is the guitar: keep its shape, color and six strings. One skeleton guitarist, [short anchor], stands at the left of the stage with the six-string electric guitar on a strap, right hand holding a pick resting on the strings and left hand on the neck, the moment before he strikes. [One or two stage details in view.] [Light, member clearly readable.] [Colors.] Medium shot at eye level, framed from the knees up with open space on the right, one figure in one scene. [Look line]
```

## Checking a band result

Use the checklist in `shots.md`, and check these first, because they fail most:

- Hands: five bone fingers each, in a position that could play the instrument.
- String and tuning peg counts. One neck per guitar.
- Drum kit pieces match the instrument block, and the drummer is seated.
- Handedness matches the bible in every guitar and bass shot.
- The right number of members, each matching the line-up: headwear, garment, color accent.
- Smooth, intact skulls.
- Gear stands where the stage plate puts it.
- The skeleton cowboy is not in the frame.

## To settle the first time the band is made

Record the answers in "Lessons" in `grok-rules.md`.

1. Does editing one member out of the line-up into a sheet work, or is a crop needed?
2. Does the line-up hold all members in the band master wide, or do member sheets need to be attached as well?
3. Do instrument counts hold with the instrument image attached, or do close-ups need an edit pass?
