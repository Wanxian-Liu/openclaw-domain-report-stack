#!/usr/bin/env python3
"""Validate project.meta.yaml and team_id against domain-teams manifest."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML required. Run: pip install -r "
        f"{Path(__file__).parent / 'requirements.txt'}",
        file=sys.stderr,
    )
    sys.exit(1)

DEFAULT_MANIFEST = (
    Path.home()
    / ".openclaw"
    / "weavevault"
    / "data"
    / "public"
    / "domain-teams"
    / "_manifest"
    / "teams.json"
)


def load_manifest(path: Path) -> list:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        teams = raw.get("teams")
        if isinstance(teams, list):
            return teams
    raise ValueError("manifest must be {schema_version, teams: []} or a JSON array")


def team_ids_registered(teams: list) -> set[str]:
    out: set[str] = set()
    for entry in teams:
        if isinstance(entry, dict) and "team_id" in entry:
            tid = entry["team_id"]
            if isinstance(tid, str) and tid.strip():
                out.add(tid.strip())
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "Usage: verify_project_meta.py <project_dir>",
            file=sys.stderr,
        )
        return 1

    project_dir = Path(sys.argv[1]).expanduser().resolve()
    meta_path = project_dir / "project.meta.yaml"

    if not meta_path.is_file():
        print(f"ERROR: missing {meta_path}", file=sys.stderr)
        return 1

    try:
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ERROR: invalid YAML: {e}", file=sys.stderr)
        return 1

    if not isinstance(meta, dict):
        print("ERROR: project.meta.yaml must be a mapping", file=sys.stderr)
        return 1

    team_id = meta.get("team_id")
    engagement = meta.get("engagement")

    if not team_id or not isinstance(team_id, str) or not team_id.strip():
        print("ERROR: team_id missing or empty", file=sys.stderr)
        return 1

    if engagement is None or (isinstance(engagement, str) and not engagement.strip()):
        print("ERROR: engagement missing or empty", file=sys.stderr)
        return 1

    manifest_path = Path(
        os.environ.get("DRS_TEAMS_MANIFEST", str(DEFAULT_MANIFEST))
    ).expanduser().resolve()

    if not manifest_path.is_file():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    try:
        teams = load_manifest(manifest_path)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR: invalid manifest JSON: {e}", file=sys.stderr)
        return 1

    registered = team_ids_registered(teams)
    tid = team_id.strip()

    if tid not in registered:
        print(
            f"ERROR: team_id not registered in manifest: {tid!r} "
            f"(manifest has {len(registered)} team(s))",
            file=sys.stderr,
        )
        return 1

    print(f"OK: project_dir={project_dir} team_id={tid} engagement={engagement!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
