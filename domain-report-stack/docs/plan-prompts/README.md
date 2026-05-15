# Plan 模式专用提示词（`docs/plan-prompts/`）

本目录为 **domain-report-stack** 各团队角色的 **完整、可独立使用** 的 Plan 提示词。每个文件对应一个 `role_id`，可直接整份粘贴到 Cursor **Plan**（或作为子代理系统提示）使用。

## 目录结构

| 团队 `team_id` | 目录 | 角色数 |
|----------------|------|--------|
| `liaoning.opc-ai-native-incubator` | `liaoning.opc-ai-native-incubator/*.plan.md` | 8 |
| `business.professional` | `business.professional/*.plan.md` | 7 |
| `built-environment.urban-culture-tourism` | `built-environment.urban-culture-tourism/*.plan.md` | 7 |

## 使用方式

1. 在仓库或 WeaveVault 中确认 `project.meta.yaml` 的 `team_id` 与本期 `engagement`。  
2. 打开 `pipelines/role-matrix/<team_id>.yaml`，按顺序或按 wave 选取角色。  
3. 将对应 **`.plan.md` 全文** 粘贴到 Plan 输入框（可附上 `inputs/`、`project.meta.yaml` 与知识库摘录）。  
4. 产出须满足各文件中的 **知识边界** 与 **引用索引** 要求。

## 与 `prompts/*.md` 的关系

- `roles/<team>/prompts/*.md`：编排用**短提示**（门禁要点）。  
- `docs/plan-prompts/<team>/*.plan.md`：Plan 重做/深度生成用**长提示**（身份、结构、自检）。

二者应保持一致边界；以本目录 Plan 文件为**完整规格**时，短提示可视为摘要。
