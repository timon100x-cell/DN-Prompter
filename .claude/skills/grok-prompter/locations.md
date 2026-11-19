# Stage 4: Locations and props

Goal: every location on Tim's shot list has a fixed location block in the bible and approved reference images in `refs/`.

Ask Tim for the list of locations first (or read it from his shot list). A place used in only one wide shot does not need references; write it straight into that shot's prompt.

## Questions for a location

One round, with suggested answers that fit the world:

- What the place is, in a few words.
- Three or four landmark features that make it recognizable (a sign, a tree, a broken window, a particular bar).
- Materials and surfaces.
- Light sources in the place, and the time of day and weather the story uses.
- Where in the place most of the action happens.
- Which states the place goes through in the story (day, night, burning, ruined, flooded...). Read them from the lyrics and suggest them.

## The location block

One or two sentences in the bible: what the place is, its landmarks with counts and positions, its surfaces. Plus a **short anchor** of a few words for use when the reference is attached. Use the same nouns everywhere.

Also write a **"must stay" line**: the shape and count of the landmarks that make the place recognizable (for the King of Nothing castle: five round towers with tall pointed crimson roofs, a narrow gate tower, a low gate about twice a man's height, grass between moat and wall, a plank bridge with railings). Every prompt that shows the place names these, even when the image is attached, because Grok leaves out what is not named and rebuilds what is not pinned.

Light is written per reference image, in the story's real lighting, because the lighting of the reference carries into every shot made from it.

## Reference images

### 1. Master wide

A new image. The empty place, no people, in the story's lighting.

```
[Location block, phrased as a wide view of the empty place.] [Landmarks with positions: left, right, foreground, background.] [Surfaces.] [Light: sources, direction, hard or soft, everything readable.] [Colors.] Wide shot at eye level showing the whole place, no people, everything sharp. [Look line]
```

### 2. Reverse angle

An edit of the master, so shots facing the other way match.

```
Show the same place from the opposite side, looking back toward where the camera stood. Keep the same [landmarks], surfaces, lighting and time of day. No people.
```

### 3. Action corner

An edit of the master: a closer view of the spot where most of the action happens.

```
Move the camera closer to [the spot], framed as a medium-wide view at eye level. Keep the same [landmarks in view], surfaces, lighting and time of day. No people.
```

### 4. Standard camera angles (main locations)

For a location that many shots use, make the camera angles before any shot, not on demand. In King of Nothing, angles made on demand rebuilt the castle (square towers, a giant gate), and Tim had to stop the shots to ask for side views first. Offer this set once and let Tim pick:

- Front (the master)
- Three-quarter from the left, and from the right
- The entrance straight on, a few steps away (gate, door, stage front)
- Low on the ground, and far away (the place small in its landscape)
- Bird's-eye
- From inside looking out, or the reverse angle

Each is an edit of the master in a new Grok chat, written as the camera moving to a named spot, with the "must stay" line and a size note against a person. Keep only results that are clearly the same building. These double as plates (below).

### 5. Story states: overview first

For every state the place goes through (night, burning, ruin), first make **one overview of the whole place in that state**, as an edit of the master, and get it approved. Every detail shot of that state is then built from that overview, never from the day master. In King of Nothing the ruin was built detail-first and drifted: the throne grew as tall as the towers, too much of the building stayed standing, and burned spikes made the horizon look like a burned forest.

In the overview prompt, say what is left and what is gone, how big the remaining large props are against the building, and what stays untouched around it ("the meadow beyond is unburnt"). Save it as `refs/<location>-<state>` and add the state to the bible.

### Variants

Another time of day or weather is an edit of the master, never a new generation:

```
Change the time to night, lit by [sources]. Keep the layout, landmarks, surfaces and framing exactly as they are.
```

Save as `refs/<location>-master`, `-reverse`, `-corner`, `-night` and so on.

### Plates (camera positions for shots)

A plate is the location from one shot's exact camera position, with nobody in it. Make one before any shot that adds a character there (see `shots.md`). Write it as the camera moving to a named spot, list the landmarks that must stay, and give a size note against a person:

```
Move the camera to [named spot], [height and direction it looks]. Keep the same [landmarks with shape and count], surfaces and light exactly as they are. [The door is about twice the height of a man.] Nobody in the scene.
```

Save as `refs/plate-<location>-<view>` and add it to the bible's plate table with its size note.

## Props

A recurring object (a guitar, a letter, a lantern) gets one clean reference: the object alone on the plain light grey background, even light, whole object in frame. Save as `refs/prop-<name>`. Attach it only to shots where the prop is in frame.

## Checklist before approving a location

- Every landmark present, with the right count and position.
- No people, no stray text, nothing from another era.
- Light matches the story's time of day and is bright enough to read the whole place.
- Reverse and corner views clearly show the same place: same landmarks, same surfaces, same light.
- Every camera angle and state overview checked against the master for the "must stay" line, one landmark at a time. A new angle that changes a tower's shape or the size of a door is a regenerate, even if it looks good.
