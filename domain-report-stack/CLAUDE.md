# domain-report-stack — Agent 强制协议

## 优先级

本文件规则高于即兴长文。即使用户要求快速出稿，仍须遵守阶段顺序与门禁。

## 何时加载

用户意图涉及：行业研究、可研、商业计划、尽调备忘、政策解读报告，或「把现有报告改到可交付」，且未明确排除本流程时，先读本文件再执行。

## 必读扩展

- 缺陷分级、评分与摘要约定：**[`docs/RUBRIC.md`](docs/RUBRIC.md)**
- Markdown 之后的导出契约：**[`docs/EXPORT.md`](docs/EXPORT.md)**
- **子代理编排（domain_deep）**：**[`docs/ORCHESTRATION.md`](docs/ORCHESTRATION.md)**

## 知识来源（唯一）

- **允许**：WeaveVault `public` 下、该 `team_id` 在 `domain-teams/_manifest/teams.json` 中登记的 `search_roots` 所指路径内的文档，以及项目目录内用户提供的 `inputs/` 等资料。
- **禁止**：将 memory-vault、memory-palace、或未列入 `search_roots` 的 WV 路径当作行业依据；禁止在未列出路径的情况下用「常识」填充行业数据。

## 每阶段引用清单

每个阶段结束前，在对话或阶段小结中列出 **本阶段引用过的 WV 文件路径**（相对 `domain-teams/`）。无清单则该阶段视为未完成。

## 执行顺序（不得跳步）

1. `intake` — 资料与元数据
2. `strategic` — 范围、成功标准、不做清单（**不使用「CEO」角色名**）
3. `adversarial` — 质询/辩论（若 pipeline 启用）
4. `domain_deep` — 领域深潜（团队蓝图 + `pipelines/role-matrix/<team_id>.yaml` + **子代理规则见下节**）
5. `synthesis` — 综合
6. `quality` — 质量评审（对齐 RUBRIC）
7. `preflight` — 交付前清单（含 P0 与总分规则）
8. `ship` — 最终中文 **Markdown**（SoT）；版式导出见 EXPORT

规则：

- 维护项目目录下 `state.json`：阶段仅按序推进。
- **无有效 `team_id`，或未在 manifest 注册，不得执行 `ship` 或声称最终交付。**
- 未经用户**明确书面**放弃门禁，不得跳过 `preflight`。
- **`engagement: generate`** 的章节结构与 **`business-plan`** 一致（见团队蓝图 YAML）。

## domain_deep 与 OpenClaw 子代理（生产默认）

当工具集包含 **`sessions_spawn`**、**`Yield`**、**`Subagents`** 时（如 profile `full`）：

1. 读取 **`pipelines/role-matrix/<team_id>.yaml`** 中的 **`domain_deep_waves`** → 当前 `engagement` 对应的 wave 列表。
2. **按 wave 串行**：对每一 wave  
   - 若 wave 内仅一个 `role_id`：发起 **一次** `sessions_spawn`，任务正文使用 **`docs/ORCHESTRATION.md`** 中的模板（填好 `PROJECT_DIR`、`TEAM_ID`、`ROLE_ID`、`ENGAGEMENT`）。  
   - 若 wave 内多个 `role_id`：对**每个** `role_id` **各** `sessions_spawn` 一次（并联），**全部 spawn 完成后调用一次 `Yield`**，等待子代理 announce；**禁止** busy-loop 轮询列表等完成。  
3. 子代理 **默认隔离上下文**；须在 spawn 任务中写清 **唯一** 的 `prompts/<role_id>.md` **绝对路径**；子代理 **禁止** Read 其它 `role_id` 的 prompt 文件。  
4. 所有 wave 完成后，主代理进入 `synthesis`，合并子代理产出（去重、对齐口径、补过渡段）。  
5. **remediation**：只对缺陷表映射到的 `role_id` spawn，不必跑满全部 wave（见 ORCHESTRATION）。

**干跑 / 用户书面要求不 spawn**：可跳过 `sessions_spawn`，在主会话内按 ORCHESTRATION「无子代理回退」顺序 Read 各 `prompts/*.md` 写稿。

**若工具集中无 `sessions_spawn`**：必须使用回退模式，不得假装已 spawn。

## remediation 与 generate

- **remediation**：按 RUBRIC 产出完整缺陷表（条数不限）与执行摘要（3–5 条指向缺陷表）；可按缺陷子集映射角色 spawn，不必七帽全跑。
- **generate**：等同 **business-plan** 章节蓝图；全流程仍走八阶段。

## OpenClaw 单会话模拟

若无法 spawn 子会话：分轮次执行，每轮只做一阶段，并更新 `state.json`；`domain_deep` 使用 ORCHESTRATION 回退模式。

## 完成定义

- `preflight` 通过；`state.json` 中八阶段均为 `done`；无未关闭 **P0**（见 RUBRIC）；最终 MD 含数据来源与局限性说明。
