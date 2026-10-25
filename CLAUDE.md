# playdate-nim-emilia

Playdate games and experiments written in Nim, made for Emilia.

## Layout

- `knowledge/` is an [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  bundle of what we learn about Playdate and Nim. See "Knowledge" below.
- `openspec/` holds OpenSpec specs (`specs/`) and proposed changes (`changes/`).
  Use the `/opsx:*` commands to plan work before writing code.
- `scripts/check_okf.py` checks that `knowledge/` is a conformant bundle.

## Knowledge

Use `/learn <what you learned>` to add or update a concept. Rules:

- One concept per file, named in kebab-case, placed in the area it is about
  (`playdate/`, `nim/`, `references/`, or a new subdirectory with its own
  `index.md`). Never name a concept `index.md` or `log.md`.
- Frontmatter must have `type`. Also set `title`, a one-sentence
  `description`, `tags`, `status`, and `generated`. Use one of these types,
  or add a new one only when none fits:
  - `Concept` explains how something works.
  - `How-To` gives steps to get something done.
  - `Gotcha` records a pitfall: symptom, cause, fix.
  - `Reference` points at external material (set `resource` to its URL).
  - `Decision` records a choice made for this project and why.
- Actors: content written by Claude uses `generated: { by: claude-code/agent, at: <ISO 8601 UTC> }`.
  Content Pietro writes or confirms uses `human:pietroppeter`. Only add a
  `verified` entry for `human:pietroppeter` when Pietro has confirmed it.
- Prefer `status: draft` for things learned once and not yet confirmed in
  practice; promote to `stable` when they hold up.
- Record where a claim came from in `sources` (with an `id`) and cite it with
  a footnote `[^id]`. Docs, forum threads, and commits in this repo all count.
- Link related concepts with bundle-relative links such as
  `[draw loop](/playdate/draw-loop.md)`. Links to concepts not written yet are fine.
- Prefer headings, lists, tables and code blocks over long prose.
- After adding or changing concepts, update the `index.md` of each touched
  directory (entry: `* [Title](file.md) - description`) and add an entry to
  `knowledge/log.md` under today's `## YYYY-MM-DD` heading, newest first.
- Run `python3 scripts/check_okf.py` before committing.
