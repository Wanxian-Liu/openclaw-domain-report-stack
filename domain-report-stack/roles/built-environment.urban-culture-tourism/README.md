# 团队：built-environment.urban-culture-tourism

**display_name**：文商旅与城市更新

## 边界

- 适用：城市更新、文旅综合体、历史文化街区、工业遗产活化、商业策划等（与 WV 知识库标签一致）。
- **禁止串台**：不得引用本团队 `search_roots` 外的 WV 路径（如农业、纯住宅开发模板）作为本项目事实依据。

## WV 对应

- Manifest：`domain-teams/_manifest/teams.json`
- 知识根：`domain-teams/knowledge/built-environment.urban-culture-tourism/`

## 角色与矩阵

- 蓝图：`pipelines/blueprints/built-environment.urban-culture-tourism.yaml`
- 顺序：`pipelines/role-matrix/built-environment.urban-culture-tourism.yaml`
- 提示词：`prompts/<role_id>.md`（七帽）

## remediation

- 先出完整缺陷表（见 `docs/RUBRIC.md`），再按缺陷映射到相关 `role_id`，**不必每次七帽全跑**。
