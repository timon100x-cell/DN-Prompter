# First real run of the tool: notes on what to improve

- 13 Nov 2026, look line: Tim wants the film feel to change per shot, but the skill assumes one fixed look line per video. Workaround used: a fixed base look line plus one per-shot film-feel sentence. The skill should support this.
- 13 Nov 2026, world questions: Tim answered "yes" to multiple-choice questions, meaning option a. Questions should mark a default ("a, recommended") so "yes" is unambiguous.
- 13 Nov 2026: Tim brought his own inspiration image before the look test. The skill has no step for that; it was saved as refs/castle-inspiration.
- 13 Nov 2026: the base look line I wrote named scene materials (wood, grass, water). That breaks on studio sheets. Look lines must name no materials; the skill's example "natural skin and fabric texture" invites this mistake.
- 13 Nov 2026: for the look test, variants B and C were given as "replace the last sentence". Tim pastes by hand, so every variant should be a full copyable prompt.
- 13 Nov 2026, first cowboy source image: Grok made the "wooden crown with flaking gold paint" as a shiny metal crown, gave 8 buttons instead of 6, and the red fissures read bright. Tim then dropped the fissures for good and changed the outfit.
- 13 Nov 2026, band master (B1): with the line-up attached, Grok copied the line-up's arrangement: five figures in a flat row facing the camera, even light, no floor shadows, so it looked pasted in. Tim: "looks fake". Also the guitar became a sunburst model since the prop was not attached. Retry: say the line-up is for clothing only, not poses or arrangement; stagger depths; turn members toward each other; light falloff and floor shadows. If this works, update band.md's master template.
