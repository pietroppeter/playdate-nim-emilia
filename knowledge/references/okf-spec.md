---
type: Reference
title: Open Knowledge Format (OKF) spec
description: The format this knowledge bundle follows, a directory of markdown files with YAML frontmatter.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags: [okf, meta]
status: stable
generated: { by: claude-code/agent, at: 2026-10-25T12:30:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: OKF SPEC.md (v0.2)
    author: team:google-cloud
---

# Summary

OKF is a format published by Google Cloud for knowledge that both people and
agents read and write. A bundle is a directory tree of markdown files; each
non-reserved file is one concept and its path (minus `.md`) is its ID.[^okf-spec]

# Rules that matter here

* Every concept needs YAML frontmatter with a non-empty `type`. That is the
  only hard requirement for conformance.
* `title`, `description`, `resource` and `tags` are recommended.
* `index.md` and `log.md` are reserved at every level. Index files have no
  frontmatter, except the bundle root, which may declare `okf_version`.
* `log.md` groups entries under `## YYYY-MM-DD` headings, newest first.
* Link concepts with ordinary markdown links, preferably bundle-relative
  (`/nim/some-concept.md`). Broken links are allowed and mean
  not-yet-written knowledge.
* Trust: `generated: { by, at }` records who wrote the content, `verified`
  records who confirmed it. Actors are `human:<id>`, `<tool>/<version>` or
  `process:<id>`. Only a `human:` verifier makes a concept human-reviewed.
* Lifecycle: `status` is `draft`, `stable` (default) or `deprecated`.
* Provenance: list `sources` with an `id` and `resource`, and cite claims
  with footnotes whose label is the source `id`.

[^okf-spec]: OKF SPEC.md (v0.2)
