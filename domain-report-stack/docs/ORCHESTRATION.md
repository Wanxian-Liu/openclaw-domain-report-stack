# domain_deep 编排（OpenClaw 子代理）

适用于主代理工具集已包含 **`sessions_spawn`**、**`Subagents`**、**`Yield`**（OpenClaw `full` profile 等）的环境。

## 路径约定

- 技能根：`SKILL_ROOT="$HOME/.openclaw/skills/domain-report-stack"`
- 角色提示词：`$SKILL_ROOT/roles/<team_id>/prompts/<role_id>.md`（`team_id` 与目录名一致，含点号）
- 波次定义：`$SKILL_ROOT/pipelines/role-matrix/<team_id>.yaml` 键 **`domain_deep_waves`** → `<engagement>` → 外层列表 = wave 序号，内层列表 = 该 wave 内可并行的 `role_id`

## 串联与并联

- **wave 之间**：严格**串行**（上一 wave 全部 announce 收齐后，再 spawn 下一 wave）。
- **同 wave 内多个 role**：**并联** — 对每个 `role_id` 各调用一次 `sessions_spawn`，然后 **调用一次 `Yield`**，等待子代理完成事件；**禁止**轮询 `/subagents list` 直到完成（见 OpenClaw 文档：push-based completion）。
- **单元素 wave**：等价于仅一个子代理，仍可在 spawn 后 `Yield` 收结果。

## 单次 `sessions_spawn` 任务文案模板

将下列占位符替换：`PROJECT_DIR`、`TEAM_ID`、`ROLE_ID`、`ENGAGEMENT`。

```text
你是 domain-report-stack 的子代理（单角色）。工作目录继承父会话。

1) 用 Read 读取全文（不得跳过）：
   $HOME/.openclaw/skills/domain-report-stack/roles/TEAM_ID/prompts/ROLE_ID.md

2) 读取项目资料目录：PROJECT_DIR/inputs/ 下用户提供的文件（按 relevance）。

3) 行业事实仅允许来自 manifest 中该 team 的 search_roots（WeaveVault domain-teams/...）及 PROJECT_DIR/inputs/；禁止其它 WV 路径与 memory-vault。

4) 只产出本 ROLE_ID 职责范围内的 Markdown 小节（中文），在文末列出本回答引用过的 WV 相对路径（相对 domain-teams/）。

5) 禁止读取其它 role_id 的 prompts/*.md。禁止替其它帽写内容。

上下文：engagement=ENGAGEMENT；team_id=TEAM_ID。
```

父代理在 `synthesis` 合并各子代理产出。

## remediation

不按完整 `domain_deep_waves`；由缺陷表映射到子集 `role_id`，对每个需修复的维度 spawn 一次（可串行），再合并进修订稿。

## 无子代理能力时的回退

若有效工具列表中**没有** `sessions_spawn`：在**主会话**内按 `domain_deep_waves` **顺序**执行，每 wave 内对各 `role_id` **顺序** Read 对应 `prompts/*.md` 再写稿（伪并联，不并行）。

## 干跑 / 用户明确豁免

用户书面声明 **干跑、不 spawn、单会话** 时：使用回退模式，不调用 `sessions_spawn`。

## 参考

- [OpenClaw Sub-agents](https://docs.openclaw.ai/tools/subagents)
- [Session tools](https://docs.openclaw.ai/concepts/session-tool)
