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

## The location block

One or two sentences in the bible: what the place is, its landmarks with counts and positions, its surfaces. Plus a **short anchor** of a few words for use when the reference is attached. Use the same nouns everywhere.

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

### Variants

Another time of day or weather is an edit of the master, never a new generation:

```
Change the time to night, lit by [sources]. Keep the layout, landmarks, surfaces and framing exactly as they are.
```

Save as `refs/<location>-master`, `-reverse`, `-corner`, `-night` and so on.

## Props

A recurring object (a guitar, a letter, a lantern) gets one clean reference: the object alone on the plain light grey background, even light, whole object in frame. Save as `refs/prop-<name>`. Attach it only to shots where the prop is in frame.

## Checklist before approving a location

- Every landmark present, with the right count and position.
- No people, no stray text, nothing from another era.
- Light matches the story's time of day and is bright enough to read the whole place.
- Reverse and corner views clearly show the same place: same landmarks, same surfaces, same light.
