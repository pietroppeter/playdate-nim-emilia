---
type: Reference
title: OpenSpec
description: Spec-driven workflow used to plan changes to the code before implementing them.
resource: https://github.com/Fission-AI/OpenSpec
tags: [openspec, tooling, meta]
status: stable
generated: { by: claude-code/agent, at: 2026-10-25T12:30:00Z }
sources:
  - id: openspec-repo
    resource: https://github.com/Fission-AI/OpenSpec
    title: Fission-AI/OpenSpec
---

# Summary

OpenSpec is a CLI (`npm install -g @fission-ai/openspec`) plus agent
commands for spec-driven development.[^openspec-repo] It lives in
`openspec/` at the repo root: `specs/` holds the current truth about what
the code does, `changes/` holds proposed changes, and archived changes move
to `changes/archive/`.

# Workflow in this repo

1. `/opsx:explore` to think an idea through without writing anything.
2. `/opsx:propose <idea>` creates `openspec/changes/<name>/` with
   `proposal.md`, spec deltas, `design.md` and `tasks.md`.
3. `/opsx:apply` implements the tasks.
4. `/opsx:archive` merges the spec deltas into `openspec/specs/` and archives
   the change. This is also the moment to condense learnings into this
   bundle with `/learn`.

# How it relates to this bundle

OpenSpec specs describe what *this project's code* must do. This bundle
holds what I *learned* about Playdate and Nim, which outlives any one change.

[^openspec-repo]: Fission-AI/OpenSpec
