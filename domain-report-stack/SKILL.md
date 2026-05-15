---
name: domain-report-stack
version: "0.2.5"
description: |
  domain-report-stack — 多领域专业报告工作流（GStack 式分层门禁）。
  触发词：domain-report-stack、领域报告、专业报告、报告改造、remediation、可研、尽调备忘、商业策划。
  知识来源仅限 WeaveVault public：domain-teams/（见 CLAUDE.md）。
  generate 默认映射 business-plan 章节蓝图。
  domain_deep 支持 OpenClaw sessions_spawn + Yield 按 wave 并联（见 docs/ORCHESTRATION.md）。
---

# domain-report-stack

自洽技能包：流程、门禁与脚本在 `~/.openclaw/skills/domain-report-stack/`；**行业事实与团队注册**在 WeaveVault：

`~/.openclaw/weavevault/data/public/domain-teams/`

## 已注册团队（示例）

| team_id | 说明 |
|---------|------|
| `built-environment.urban-culture-tourism` | 文商旅与城市更新；蓝图与角色见 `pipelines/blueprints/`、`pipelines/role-matrix/`、`roles/built-environment.urban-culture-tourism/` |
| `digital-culture.ai-native-ip-studio` | AI 原生态一人公司 + 阅文 IP + 杭武协同 + AIGC 短剧/动画；见 `pipelines/blueprints/digital-culture.ai-native-ip-studio.yaml`、`roles/digital-culture.ai-native-ip-studio/`、`domain-teams/knowledge/digital-culture.ai-native-ip-studio/` |
| `business.professional` | 专业商业与投融资（通用 B2B、融资与尽调向）；蓝图与角色见 `pipelines/blueprints/business.professional.yaml`、`pipelines/role-matrix/business.professional.yaml`、`roles/business.professional/`、`domain-teams/knowledge/business.professional/` |
| `liaoning.opc-ai-native-incubator` | **辽宁主线**：OPC（AI 原生一人公司）× 政府合作 × 多业态孵化与就业平台；见 `pipelines/blueprints/liaoning.opc-ai-native-incubator.yaml`、`pipelines/role-matrix/liaoning.opc-ai-native-incubator.yaml`、`roles/liaoning.opc-ai-native-incubator/`、`domain-teams/knowledge/liaoning.opc-ai-native-incubator/` |

## 两轨 engagement

| 轨道 | 说明 |
|------|------|
| **generate** | 完整生成链；**章节顺序与 `business-plan` 相同**（见团队蓝图）。 |
| **remediation** | 研读已有稿 → 缺陷表（P0–P3）与评分 → 修订；门禁与 generate 对齐（见 `docs/RUBRIC.md`）。 |

其他 `engagement`：`feasibility`、`business-plan`、`due-diligence`、`policy-memo` 等见 `schemas/project.meta.schema.json` 与团队蓝图。

## 交付分层

- **ship**：通过 preflight 的**中文 Markdown**（唯一真相源）。
- **Word / PPT / PDF**：可插拔导出技能，见 **`docs/EXPORT.md`**（不绑定具体厂商）。

## Plan 模式长提示词

各团队、各角色**可独立粘贴到 Cursor Plan** 的完整提示词见 **`docs/plan-prompts/`**（`README.md` + 每角色 `*.plan.md`）；与 `roles/<team>/prompts/*.md` 短提示互补。

## 与 WV 的关系

- 团队必须在 `_manifest/teams.json` 注册；未注册则 `verify_project_meta.py` 失败。
- 脚本不 rglob OpenClaw 其他目录下的 markdown。

## 重命名

若重命名技能目录或 WV 根目录 `domain-teams`，请同步更新 `scripts/verify_project_meta.py` 默认 manifest 路径及 `CLAUDE.md` 中的路径描述；并保持本文件 frontmatter `name` 与目录名一致。
