# scripts/

## 依赖

```bash
pip install -r requirements.txt
```

（仅需 PyYAML。）

## verify_project_meta.py

校验项目目录下的 `project.meta.yaml`：

- 必填：`team_id`、`engagement`
- `team_id` 必须在 manifest 的 `teams[]` 中注册（`team_id` 字段精确匹配）

默认 manifest：

`~/.openclaw/weavevault/data/public/domain-teams/_manifest/teams.json`

覆盖方式：

```bash
export DRS_TEAMS_MANIFEST=/path/to/custom-teams.json
python3 verify_project_meta.py /path/to/project
```

## init_state.py

生成 `state.json`（八阶段全 `pending`）。若存在 `project.meta.yaml` 且含 `slug`，写入 `project_slug`。

```bash
python3 init_state.py /path/to/project
python3 init_state.py /path/to/project --force
```

## TODO

- 对接 `wv search` CLI，按 `search_roots` 做检索辅助（后续步骤）。
