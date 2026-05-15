# next_action（未来脚本，本步无代码）

## 目的

减少主代理跳步：根据 `state.json` 与 `project.meta.yaml` 打印**下一步**应执行的阶段、须读取的蓝图/角色、以及禁止事项。

## 设想接口

```bash
# 未来示例
python3 scripts/next_action.py <project_dir>
```

## 输出示例（概念）

- `current_stage`: 下一待完成阶段 id
- `read_first`: `CLAUDE.md`, `pipelines/blueprints/<key>.yaml`, `docs/RUBRIC.md`（若 remediation）
- `blockers`: 若有未关闭 P0，提示不得 ship

本步仅保留文档；实现可在第三步及以后加入。
