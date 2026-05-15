# 团队角色包：`liaoning.opc-ai-native-incubator`

**对外名称**：辽宁 · OPC（AI 原生一人公司）政府合作孵化与就业平台

## 1. 团队定位与适用范围

本角色包用于在**辽宁省政策与产业语境**下，撰写或修订以**政府合作**为前提、以**OPC（AI 原生一人公司）**为核心对象的**平台型**商业策划、可研、尽调备忘与政策合规备忘。分析对象包括：政府—平台公司—入驻主体之间的**责任界面**、多种业态组合（playbook）、人才与用工链路、AI 与数据合规、商业可持续与风险披露。

## 2. 知识来源与边界（强制）

- **Manifest**：`domain-teams/_manifest/teams.json`
- **授权知识根**：`domain-teams/knowledge/liaoning.opc-ai-native-incubator/`

凡属事实性主张（政策条文、财政安排、落地案例、统计数据），**仅能**以上述知识根内已收录材料为据；缺证处须标注为**假设**或**待核实**，不得外推为「辽宁已生效」或「本项目已确定」。

## 3. 编排与工件

| 工件 | 路径 |
|------|------|
| 章节蓝图 | `pipelines/blueprints/liaoning.opc-ai-native-incubator.yaml` |
| 角色顺序与并行波次 | `pipelines/role-matrix/liaoning.opc-ai-native-incubator.yaml` |
| 角色提示词（八帽） | `prompts/<role_id>.md` |

`remediation` engagement 时，按 `docs/RUBRIC.md` 产出缺陷表并按维度映射角色，**不要求八帽全量执行**。

## 4. 与 `business.professional` 的协同

若项目需要**长篇幅投融资模型、详细财务报表或资本市场叙事**，应在 `project.meta.yaml` 中通过 `team_id` 切换或拆分独立 engagement，由 `business.professional` 角色包承担；本包**不得**引用未列入本团队 `search_roots` 的外部知识路径作为本项目事实依据。

## 5. 文体与专业度基线

- 默认文体：**决策备忘录 / 可研附件 / 商业计划书章节**体例；避免宣传口号与未定义缩写堆砌。
- 每一事实句尽量可追溯至**具体文件路径 + 段落/条款要点**；无法溯源时标明不确定性。
- 对政府合作、劳动用工、数据与内容安全等议题，保持**合规披露**语气：列风险、列缓解、列责任主体，**不提供**替代正式法律或审计意见的「结论性背书」。
