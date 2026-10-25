# playdate-nim-emilia
Making play date stuff for Emilia

## How this repo is organized

- `knowledge/`: what we learn about Playdate and Nim, condensed as an
  [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  bundle. Add to it with `/learn <what you learned>` in Claude Code, and check it
  with `python3 scripts/check_okf.py`.
- `openspec/`: [OpenSpec](https://github.com/Fission-AI/OpenSpec) specs and
  change proposals. In Claude Code use `/opsx:explore`, `/opsx:propose`,
  `/opsx:apply` and `/opsx:archive`. The CLI is `npm install -g @fission-ai/openspec`;
  cloud sessions install it automatically through `.claude/hooks/session-start.sh`.
