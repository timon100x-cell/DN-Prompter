# Stage 5: Shot prompts

Goal: an approved still for every shot on Tim's list. Each still is the start frame of a video clip.

## Where the shots come from

Shots come from the approved plan for a section (`song-map.md`). Never write shot prompts for a section whose plan Tim has not approved. If Tim pastes his own list instead, put it into the shot table against the song map, ask one short question where a line does not say who, where or how close, and show it back as the plan.

Before writing, check that every plate and story-state overview the section needs exists. Make those first.

## Handing over a section

- Each shot: its number and one line from the plan, a settings line ("New chat. 16:9, 2K. Attach: 1 Castle, front, 2 Merchant sheet"), the image prompt in its own code block, then "Video:" and the video prompt in its own code block (rules in `grok-rules.md`), then at most three things to check.
- Use the plain names from the bible's reference table for attachments, exactly as they appear on the gallery page. Never "picture A" or "your result of clip 6" without also giving the name to save it under.
- **Up to three shots go in the chat message. More than three go in a file** in the project files folder (`/mnt/project-files/<video>/<section>-prompts.md`), attached to a short message that says where to start and which shots depend on others. Keep the file in step: when a prompt changes, update the file and say so.
- Say which shots depend on another result ("make 17 before 18, because 18 is built on it").

## Matching results to shots

When Tim sends an image, the first words of the reply name the shot it is checked as ("Shot C4, the trapdoor: approved"). If two results arrive close together, or it is unclear which prompt an image belongs to, ask in one line instead of guessing.

## Shots with a character in a location: plate, then add

Use the two-step method in `grok-rules.md` ("Putting a character in a location") for every shot that puts a sheet character in a location. Check the bible's plate table first; if no plate exists for that camera position, write the plate prompt and get it approved before the add prompt.

Add template (attach 1 plate, 2 sheet, 3 prop if close to camera):

```
Add [short anchor] from Image 2 to Image 1. [He/She] [pose just before the action, where in the plate, facing what]. [Size against a landmark in the plate.] [Anything held or changed; a door or hatch that opens stays "the same size as in Image 1".] Use Image 2 only for [his/her] [face, headwear] and clothing, not its light or pose. Light [him/her] with the [light] already in Image 1, with a soft shadow on the ground under [his/her] feet[ and fog around the ankles]. Keep [landmarks], the camera position and the framing of Image 1 exactly as they are.
```

The add prompt carries no look line and no composition sentence: the plate already has them.

## Building a shot prompt (no plate)

Use this for shots without a sheet character, or where Tim wants a fresh build.

1. Decide the references: the location view that matches the camera direction (master, reverse or corner), then the sheet of each character in frame, then a prop only if it is in frame. Two or three in total.
2. Write the role lines, one per attached image.
3. Write the six sentences in the fixed order from `grok-rules.md`, using short anchors for anything that has a reference attached and full blocks for anything that does not. Name the location's "must stay" landmarks that are in view, even with the location attached.
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

Compare the image with the prompt and with the master images it was built from, side by side, not with your taste. Go through the list in this order and report only failures:

1. **Same place.** Every item on the location's "must stay" line, one by one: shape and count of towers, roofs, doors, windows, the bridge, how big the door is next to a person. If the place was rebuilt, it is a regenerate, however good it looks.
2. **Every named landmark present.** Anything the shot needs that is missing (a bridge, a moat) fails.
3. **Same props.** Big props match their earlier shots in shape and size (the throne keeps its shape; it is smaller than the gate).
4. **Character matches the sheet:** marks, side, headwear, garments. Skulls smooth and intact.
5. **Facing and eyeline.** A character who talks to, looks at or reaches for something faces it.
6. **Scale.** The character's size against the landmark named in the prompt.
7. **Light from the scene, not the studio.** The character has the scene's light and a shadow on the ground. A close-up has the same light as the wide shot it came from.
8. **Background fits the world.** Nothing added on the horizon or behind that the world does not have.
9. **State and time.** Matches the section in the song map (night stays night, smoke sky stays smoke sky).
10. Counts, hands, fingers, instruments, no sheet panels, no stray text.
11. Works as a start frame: stable pose, no motion blur.

Then answer Approved, Edit or Regenerate as described in SKILL.md. **Approve only when every point passes.** If something cannot be judged from the image (too small, too dark), say "Check X before you keep it" instead of approving. An approval taken back costs Tim more than a question.

## Logging

After each approved shot add an entry to `prompts.md`: shot number, attachments in order, the final prompt, the video prompt, any edit prompts used, the saved image name. Update the shot's status in the bible's shot table, and add its setup to "Setups used". If Tim uploads the approved still, it does not need to go into `refs/`; only references live there.
