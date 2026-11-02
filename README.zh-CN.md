# OhMyTaste

[English README](README.md)

OhMyTaste 是一个用于**基于真实文献发现科研选题**的开源 Agent Skill。用户只需要提供研究方向，它会先调查真实文献，再建立局部领域判断，提出机制驱动的研究假设，主动寻找反证和高度相似工作，审查数据、Baseline、算力与实现条件，最后最多给出一个主 Idea 和一个具有实质差异的备选 Idea。

v0.1.0-alpha.1 的目标是建立严谨、可复现、可批判的科研选题工作流。项目不宣称已经具备专家级科研判断能力，也不保证任何 Idea 的绝对新颖性。

## 项目概览

许多科研 Idea 工作流从头脑风暴开始。OhMyTaste 从证据开始。它面向科研早期选题阶段：用户可能只有一个宏观领域，也可能已经有一个细分方向，但无需准备论文清单、已有 Idea 或研究假设。

支持两种输入：

- **宏观领域**：先比较多个细分切口，再选择一个值得深入调查的方向。
- **细分方向**：跳过方向收敛，直接进入文献调查。

最终输出是一份精简研究 Proposal，并明确给出证据来源、不确定性、反向审查、可行性条件和最小判别实验。

## 为什么需要 OhMyTaste

OhMyTaste 遵循八条核心原则：

1. **Evidence before Ideas**：先检索并核查真实论文，再生成 Idea。
2. **Research taste**：优先寻找重要且尚未充分解决的问题，降低“流行技术拼接”的权重。
3. **Mechanism-driven**：建立现象、机制、干预和可检验预测之间的联系。
4. **Adversarial review**：主动寻找重复工作、反向证据和更简单解释。
5. **Feasibility first**：核查数据、Baseline、算力、设备和实现路径。
6. **Minimal decisive experiment**：优先设计能够区分竞争性解释的最小实验。
7. **Honest uncertainty**：分别标注文献事实、文献支持的判断、研究假设和未知信息。
8. **No forced ideas**：证据不足时允许明确不给出推荐。

项目不依赖自我打分、复杂术语堆叠或多 Agent 辩论制造“专家感”。最终决策依赖证据门槛和明确的否决理由。

## 核心工作流

1. **Research Direction Convergence**：针对宏观方向比较研究价值、瓶颈、近期条件变化和验证成本，选出一个细分切口。
2. **Literature Grounding**：覆盖奠基性论文、近期代表工作、最接近的方法、负面结果和挑战主流结论的证据。
3. **Field Judgment**：判断领域真正解决了什么、哪些机制仍不清楚、已有方法为何未解决核心问题。
4. **Idea Generation**：从真实研究问题出发，构造少量机制明确、可验证的候选假设。
5. **Adversarial Review**：独立反向检索高度相似工作、反证、更简单解释、数据泄漏、评测偏差和不公平 Baseline。
6. **Feasibility Audit**：核查公开数据、可复现 Baseline、资源条件、实现路径以及实验的判别能力。
7. **Final Decision**：候选 Idea 标记为 `ACCEPT`、`REVISE` 或 `REJECT`；默认只推荐一个主 Idea，最多增加一个实质不同的备选。
8. **Research Proposal**：生成 Markdown 与 LaTeX；只有环境确实存在 XeLaTeX 且编译成功时才生成并报告 PDF。

可执行流程见 [`skills/ohmytaste/SKILL.md`](skills/ohmytaste/SKILL.md)。证据与检索协议见 [`evidence-and-search.md`](skills/ohmytaste/references/evidence-and-search.md)，研究判断与反向审查规则见 [`taste-and-critique.md`](skills/ohmytaste/references/taste-and-critique.md)。

## 安装

当前 skills CLI 需要 Node.js 22.20 或更高版本。

先检查仓库能否被发现：

```bash
npx skills add arce-star/ohmytaste-skill --list
```

安装 OhMyTaste：

```bash
npx skills add arce-star/ohmytaste-skill --skill ohmytaste
```

以 Codex 为例进行全局非交互安装：

```bash
npx skills add arce-star/ohmytaste-skill --skill ohmytaste -g -a codex -y
```

本地构建独立 ZIP：

```bash
python scripts/package_skill.py --output dist/ohmytaste-v0.1.0-alpha.1.zip
```

## 使用示例

### 宏观领域输入

> 使用 OhMyTaste 调查 mechanistic interpretability 中值得研究的问题。我没有论文清单和已有假设。先比较几个细分方向，再选择一个深入调查并输出 Proposal。

### 细分方向输入

> 使用 OhMyTaste 调查神经网络 delayed generalization（grokking）。寻找一个仍然真实开放的问题，主动检索相似工作与反证，并设计能够推翻核心假设的最小实验。

### 允许拒绝推荐

> 调查 RAG evaluation。如果现有文献不足以支持一个可信的机制级新 Idea，请明确输出“没有足够可靠的推荐”，不要强行生成。

## 架构

```text
ohmytaste-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── skills/
│   └── ohmytaste/
│       ├── SKILL.md
│       ├── references/
│       │   ├── evidence-and-search.md
│       │   └── taste-and-critique.md
│       └── assets/
│           └── research-proposal.tex
├── scripts/
│   ├── check_repo.py
│   └── package_skill.py
├── evals/
│   ├── README.md
│   └── test-cases.md
├── tests/
│   ├── test_check_repo.py
│   └── test_package_skill.py
└── .github/workflows/ci.yml
```

按照 Agent Skills 规范，Skill 目录名需要与 `SKILL.md` frontmatter 中的 `name` 保持一致，因此安装名 `ohmytaste` 对应 `skills/ohmytaste/`。

## 局限性

- 无法保证绝对新颖性。数据库覆盖、付费墙、索引延迟和未公开工作都可能造成 prior art 漏检。
- 对论文全文不可访问时，只能标记为 `abstract-only`，不能据此声称核查了具体实验、图表或推导。
- 本 Skill 不能替代领域专家、实验室经验、安全审查和正式同行评议。
- 用户未提供算力、数据权限、实验设备或时间预算时，对应资源必须记为 `Unknown`。
- 即使 Proposal 通过当前审查，真实实验仍可能失败；工作流强调让失败尽早出现，并且具有判别信息。

## 开发

运行结构检查和单元测试：

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```

生成确定性 ZIP：

```bash
python scripts/package_skill.py --output dist/ohmytaste-v0.1.0-alpha.1.zip
```

从本地仓库验证 skills CLI 发现：

```bash
npx skills add . --list
```

CI 会执行仓库结构验证、单元测试、ZIP 打包、skills CLI 发现测试和非交互安装 smoke test。若 CI 环境存在 XeLaTeX，还会编译 LaTeX Proposal 模板；环境缺失时会明确记为可选检查跳过。

评测案例见 [`evals/test-cases.md`](evals/test-cases.md)。每个案例包含明确通过/失败标准。除非未来确实完成人工专家评审并留下记录，项目不会声称已经完成该类评审。

## 贡献

欢迎提交能够提高证据质量、可证伪性、可复现性或评测覆盖率的修改。工作流变更应增加或更新对应评测案例；检索和证据规则变更应说明所针对的具体失败模式。

请避免仅为了显得复杂而引入框架、评分系统或额外 Agent。

## 许可证

MIT License，详见 [`LICENSE`](LICENSE)。
