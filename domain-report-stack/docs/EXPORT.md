# 导出约定（可插拔）

## 原则

- **单一真相源**：`ship` 阶段交付通过 preflight 的**中文 Markdown**。
- **Word / PPT / PDF**：由**单独技能或人工排版**完成；本技能**不绑定**具体厂商或 CLI。

## 输入（建议）

| 字段 | 说明 |
|------|------|
| `md_path` | 已定稿 Markdown 路径 |
| `template_id` | 模板标识（团队或客户维度） |
| `format` | `docx` \| `pptx` \| `pdf` |

## 输出

- 客户向版式文件；**不改变** MD 中的事实与结论，仅做呈现层增强。

## 示例（非唯一）

- 若环境中已安装 OpenClaw 的 Minimax docx/pptx 等技能，可作为导出实现之一；实现方可替换为 Pandoc、内部模板引擎或「专业排版小组」流程。

## 状态

实现见 `scripts/export_placeholder.md`；本仓库不内置转换代码。
