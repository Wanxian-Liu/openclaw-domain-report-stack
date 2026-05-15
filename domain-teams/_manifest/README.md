# teams.json 注册说明

`teams.json` 根对象固定为：

```json
{
  "schema_version": 1,
  "teams": [ /* ... */ ]
}
```

## `teams[]` 每条记录必填字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `team_id` | string | 与 `project.meta.yaml` 中完全一致 |
| `display_name` | string | 展示名 |
| `search_roots` | string[] | 相对 `domain-teams/` 的路径前缀；检索与引用仅允许此集合内 |
| `chapter_blueprint_key` | string | 技能内蓝图：`pipelines/blueprints/<chapter_blueprint_key>.yaml` |

可选扩展：`rubric_path`、`forbidden_terms` 等。

## 已注册示例

- `built-environment.urban-culture-tourism` → `chapter_blueprint_key` 为 `built-environment.urban-culture-tourism`，对应技能内文件：  
  `~/.openclaw/skills/domain-report-stack/pipelines/blueprints/built-environment.urban-culture-tourism.yaml`
