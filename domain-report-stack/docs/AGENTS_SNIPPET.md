# 可复制到 OpenClaw `AGENTS.md` 的片段

当用户任务属于 **domain-report-stack**（多领域专业报告、可研、尽调备忘、报告改造等）时：

1. **必须先读取** `~/.openclaw/skills/domain-report-stack/CLAUDE.md` 与 **`docs/RUBRIC.md`**，再开始产出。
2. **按项目目录下的 `state.json` 推进**：一次只推进一个阶段；更新阶段状态后再进入下一阶段。
3. **禁止跳过 `preflight`** 进入最终交付，除非用户在同一对话中**明确书面**声明放弃门禁。
4. **`team_id` 必须在** `~/.openclaw/weavevault/data/public/domain-teams/_manifest/teams.json` **中注册**；未注册则不得输出「最终定稿」类交付，仅可做资料整理或提示用户注册团队。
5. 行业事实仅允许来自 manifest 中该团队的 `search_roots` 与项目 `inputs/`，不得从未声明的 WV 路径或 memory-vault 引用。
6. **`engagement: generate`** 的章节结构与 **`business-plan`** 一致；存在未关闭 **P0** 不得宣称定稿（见 RUBRIC）。
7. **`domain_deep` 阶段**（工具含 `sessions_spawn` 时）：必读 `~/.openclaw/skills/domain-report-stack/docs/ORCHESTRATION.md`；按 `pipelines/role-matrix/<team_id>.yaml` 的 **`domain_deep_waves`** 分 wave 执行；同 wave 多角色则 **多次 `sessions_spawn` 后一次 `Yield`**，不得轮询死等。
8. 每次 spawn 的任务正文须包含 **该 role 唯一** 的 `prompts/<role_id>.md` **绝对路径**，并禁止子代理读取其它角色的 prompt 文件。
9. 用户**书面**「干跑 / 不 spawn / 单会话」时：`domain_deep` 改用 CLAUDE 中的**回退模式**（主会话顺序 Read prompts）。
10. 若有效工具列表中**无** `sessions_spawn`：`domain_deep` **必须**使用回退模式。

## 与完整 AGENTS 块的关系

可将此前提供的「## domain-report-stack…」长段与本段 **合并**：本段 **7–10** 专门约束 **子代理与并联**。
