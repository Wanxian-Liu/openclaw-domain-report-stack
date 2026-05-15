#!/usr/bin/env python3
"""Create state.json with eight pending stages for a project directory."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
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

STAGE_IDS = [
    "intake",
    "strategic",
    "adversarial",
    "domain_deep",
    "synthesis",
    "quality",
    "preflight",
    "ship",
]


def load_slug(project_dir: Path) -> str:
    meta_path = project_dir / "project.meta.yaml"
    if not meta_path.is_file():
        return project_dir.name
    try:
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return project_dir.name
    if isinstance(meta, dict):
        slug = meta.get("slug")
        if isinstance(slug, str) and slug.strip():
            return slug.strip()
    return project_dir.name


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize state.json")
    parser.add_argument("project_dir", type=Path, help="Project root directory")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing state.json",
    )
    args = parser.parse_args()

    project_dir = args.project_dir.expanduser().resolve()
    project_dir.mkdir(parents=True, exist_ok=True)
    state_path = project_dir / "state.json"

    if state_path.exists() and not args.force:
        print(f"ERROR: {state_path} exists; use --force to overwrite", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    slug = load_slug(project_dir)

    state = {
        "schema_version": 1,
        "project_slug": slug,
        "stages": [
            {
                "id": sid,
                "status": "pending",
                "wv_refs": [],
                "updated_at": now,
            }
            for sid in STAGE_IDS
        ],
    }

    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: wrote {state_path} project_slug={slug!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
