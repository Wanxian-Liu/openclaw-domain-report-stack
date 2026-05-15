# domain-teams（WeaveVault public）

本目录树为 **domain-report-stack** 技能的公共知识根：团队注册、检索根路径与各团队 `knowledge/`。

## 已注册团队

| team_id | display_name | search_roots |
|---------|--------------|--------------|
| `built-environment.urban-culture-tourism` | 文商旅与城市更新 | `knowledge/built-environment.urban-culture-tourism/` |
| `digital-culture.ai-native-ip-studio` | 数字文创 · AI 原生态一人公司与 IP 短剧生态 | `knowledge/digital-culture.ai-native-ip-studio/` |
| `business.professional` | 专业商业与投融资 | `knowledge/business.professional/` |
| `liaoning.opc-ai-native-incubator` | 辽宁 · OPC 政府合作孵化与就业平台 | `knowledge/liaoning.opc-ai-native-incubator/` |

## 与技能的关系

- 技能路径：`~/.openclaw/skills/domain-report-stack/`
- Manifest：`domain-teams/_manifest/teams.json`
- 项目侧：`project.meta.yaml` 中的 `team_id` 必须与 manifest **完全一致**。

## 布局

```
domain-teams/
  INDEX.md
  _manifest/
    teams.json
    README.md
  knowledge/
    built-environment.urban-culture-tourism/   ← 首个团队知识（含 市场规模.md、文旅地产.md 等）
    digital-culture.ai-native-ip-studio/       ← AI 原生态一人公司 + IP 短剧 / 杭武协同骨架
    business.professional/                     ← 通用商业、融资与尽调口径骨架
    liaoning.opc-ai-native-incubator/          ← 辽宁 OPC × 政府合作 × 多业态孵化骨架
```
