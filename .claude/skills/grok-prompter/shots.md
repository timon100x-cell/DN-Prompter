# Stage 5: Shot prompts

Goal: an approved still for every shot on Tim's list. Each still is the start frame of a video clip.

## Taking in the shot list

Tim brings the shot list. Save it in the bible as a numbered table (number, his one-line description, location, characters, status). Do not rewrite his shots or add new ones. If a line does not say who, where or how close, ask one short question, or pick the obvious reading and say so.

Work through the list in order unless Tim names a shot. For speed he can ask for a batch ("shots 4 to 8"); give each prompt in its own code block.

## Building a shot prompt

1. Decide the references: the location view that matches the camera direction (master, reverse or corner), then the sheet of each character in frame, then a prop only if it is in frame. Two or three in total.
2. Write the role lines, one per attached image.
3. Write the six sentences in the fixed order from `grok-rules.md`, using short anchors for anything that has a reference attached and full blocks for anything that does not.
4. Make it a start frame: the moment just before the action, with room in the frame for the movement.
5. End with "one figure in one scene" (or the right count) and the look line.

Template:

```
Image 1 is the location: keep its layout, [landmarks] and lighting. Image 2 is the character sheet: use it for [his/her] [head or face], [headwear or hair] and clothing only. [Subject: count + short anchor + pose just before the action + where in the location.] [Details: what is held or worn differently in this shot, focal point.] [Art direction: two or three props or surfaces in view.] [Light: source, direction, hard or soft, subject clearly readable.] [Color: subject colors against background colors.] [Composition: shot size, camera height, what the frame cuts off, where the open space is], one figure in one scene. [Look line]
```

Worked example (invented world):

```
Settings: 16:9, 2K. Attach in this order: 1 night-market-corner, 2 mara-yellow-coat-sheet

Image 1 is the location: keep its layout, signs and lighting. Image 2 is the character sheet: use it for her face, hair and clothing only. One woman, the same character, stands under the awning of the noodle stall, holding a paper cup in both hands and looking down the street to the left. She wears her mustard-yellow coat with the collar turned up. Steam rises from two pots behind her, and rain runs off the awning edge. Warm lantern light falls on her face from the right, with cool blue light from the wet street behind, and her face stays clearly readable. Mustard yellow and warm orange against deep teal. Medium shot at eye level, framed from the waist up with open space on the left, one figure in one scene. Photoreal 35mm film still with fine grain, everything in the focal plane sharp.
```

A shot with no reference available (a one-off place or a passing figure) uses the plain six sentences with full descriptions.

## Shot size words

Use these consistently so Tim's list and the prompts match:

| Tim says | Write |
| --- | --- |
| extreme wide, establishing | Extreme wide shot, the figure small in the frame |
| wide, full body | Wide shot, the figure visible head to foot |
| medium | Medium shot, framed from the waist up |
| close-up | Close-up, framed from the shoulders up |
| extreme close-up, detail | Extreme close-up on [the one thing] |

Always add camera height (eye level, low angle, high angle) and where the open space is.

## Checking a result

Compare the image with the prompt, line by line. Report only failures.

- Right subject, right count of figures.
- Character matches the sheet: marks, side, headwear, garments.
- Location matches the reference: landmarks, layout, light.
- Every named prop present, with the right count.
- Subject bright enough to read.
- Framing as asked, with the open space where the motion will go.
- It works as a start frame: stable pose, the moment before the action, no motion blur.
- No sheet panels, no stray text, no extra limbs or fingers.

Then answer Approved, Edit or Regenerate as described in SKILL.md.

## Logging

After each approved shot add an entry to `prompts.md`: shot number, attachments in order, the final prompt, any edit prompts used, the saved image name. Update the shot's status in the bible. If Tim uploads the approved still, it does not need to go into `refs/`; only references live there.
