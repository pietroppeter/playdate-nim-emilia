---
description: "Condense something learned into the OKF knowledge bundle"
argument-hint: "<what you learned, or a topic to summarize from this session>"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 scripts/check_okf.py)
---

Capture this in the knowledge bundle under `knowledge/`: $ARGUMENTS

If no text was given, condense what was learned in this session (things that
surprised us, fixes that took effort, how an API actually behaves).

1. Read `knowledge/index.md` and the `index.md` of the likely area. Search
   `knowledge/` for an existing concept on the same thing. Update it rather
   than creating a duplicate.
2. Write or update the concept following the "Knowledge" rules in `CLAUDE.md`
   (frontmatter, type, actors, sources with footnotes, bundle-relative links).
   Keep each concept to one idea; split if it covers several.
3. Update the `index.md` of every directory you touched and add a line to
   `knowledge/log.md` under today's date.
4. Run `python3 scripts/check_okf.py` and fix anything it reports.
5. Reply with the concept paths you created or changed and a one-line summary
   of each.
