# OpenClaw — domain-report-stack + public domain-teams

This repository mirrors the **domain-report-stack** OpenClaw skill and the **public** WeaveVault `domain-teams/` knowledge roots used with it.

## Layout

- `domain-report-stack/` — skill (pipelines, roles, schemas, docs, scripts, `SKILL.md`, `CLAUDE.md`).
- `domain-teams/` — WeaveVault public manifest + per-team `knowledge/` (e.g. Liaoning OPC, business professional).

## Install (local)

Copy into your OpenClaw paths (adjust if your layout differs):

```bash
cp -a domain-report-stack ~/.openclaw/skills/domain-report-stack
mkdir -p ~/.openclaw/weavevault/data/public
cp -a domain-teams ~/.openclaw/weavevault/data/public/domain-teams
```

Then point `verify_project_meta.py` / `CLAUDE.md` at your `domain-teams/_manifest/teams.json` (defaults already assume `~/.openclaw/weavevault/data/public/domain-teams`).

## License

See `LICENSE` (MIT) unless individual files state otherwise.
