# OhMyTaste

[English README](README.md)

OhMyTaste 是一个用于**基于真实文献发现科研机会**的开源 Agent Skill。用户只需要提供宏观领域或细分研究方向，它会调查真实文献，建立领域局部地图，识别未解决的机制张力，从证据中推导候选假设，再主动寻找高度相似工作、反向证据和更简单解释，最后给出最多一个主 Idea 和一个具有实质差异的备选 Idea。

`0.1.1-alpha.1` 重点修复真实测试中暴露出的一个问题：模型可能越来越会否决弱 Idea，却没有同步提升发现更深层研究机会的能力。新版本要求所有未解决问题都必须进入后续处理，并在初始候选全部失败后执行一次有边界的 residual opportunity recovery。

项目不宣称已经具备专家级科研判断能力，也不保证任何 Idea 的绝对新颖性。

## 项目概览

许多科研 Idea 工作流从头脑风暴开始。OhMyTaste 从证据开始。它面向科研早期选题阶段：用户可能只有一个宏观领域，也可能已经有一个细分方向，但无需准备论文清单、已有 Idea 或研究假设。

支持两种输入：

- **宏观领域**：先比较多个细分切口，再选择一个值得深入调查的方向。
- **细分方向**：跳过方向收敛，直接进入文献调查。

最终输出是一份精简研究 Proposal，或者一份有明确依据的 `NO RECOMMENDATION` 判定。

## 为什么需要 OhMyTaste

OhMyTaste 当前强调以下原则：

1. **Evidence before Ideas**：先检索并核查真实论文，再生成 Idea。
2. **Opportunity discovery before filtering**：优先寻找矛盾、解耦、隐藏假设、边界反转、测量失效、机制欠定以及新出现的观测/干预能力。
3. **Mechanism-driven**：建立现象、潜在机制、干预、判别性预测和测量之间的联系。
4. **Adversarial review**：主动寻找重复工作、反向证据和更简单解释。
5. **Feasibility first**：核查数据、Baseline、算力、设备和实现路径。
6. **Minimal decisive experiment**：优先设计能够真正改变研究决策的最小实验。
7. **Honest uncertainty**：分别记录认识论类型、证据强度和访问等级。
8. **No forced ideas**：证据不足时允许明确不给出推荐。
9. **Bounded recovery**：初始候选全部失败后，只允许进行一次基于失败证据的深层发现，不允许无休止补 Idea。
10. **Scientific openness 与 project strategy 分离**：科学问题仍然开放，并不自动意味着值得现在投入。

项目不依赖自我打分、复杂术语堆叠或多 Agent 辩论制造“专家感”。最终决策依赖证据链和明确的否决理由。

## 核心工作流

1. **Research Direction Convergence**：针对宏观方向比较研究价值、瓶颈、近期条件变化和验证成本，选出一个细分切口。
2. **Literature Grounding and Scope Map**：覆盖奠基性论文、近期代表工作、最接近的方法、负面结果、挑战主流结论的证据，并记录每个核心结果真正覆盖的任务、数据、模型、loss、尺度和评测范围。
3. **Field Judgment, Tension Map, and Unresolved-Question Ledger**：判断领域真正解决了什么，同时显式记录所有仍未闭合的问题。
4. **Opportunity Discovery and Candidate Formulation**：从文献张力中生成少量候选，并为每个重要候选生成 `Discovery Trace`。
5. **Adversarial Review**：独立反向检索高度相似工作、反证、更简单解释、数据泄漏、评测偏差和贡献坍缩。
6. **Residual Opportunity Recovery and Feasibility Audit**：若所有初始候选失败，执行一次 recovery；随后核查数据、Baseline、资源和实验可行性。
7. **Final Decision**：分别输出 `Scientific Status`、`Project Priority`，并保留兼容的 `ACCEPT`、`REVISE`、`REJECT`、`NO RECOMMENDATION` 决策。
8. **Research Proposal**：生成 Markdown 与 LaTeX；只有环境确实存在 XeLaTeX 且编译成功时才生成并报告 PDF。

可执行流程见 [`skills/ohmytaste/SKILL.md`](skills/ohmytaste/SKILL.md)。证据与检索协议见 [`evidence-and-search.md`](skills/ohmytaste/references/evidence-and-search.md)，研究机会发现与反向审查规则见 [`taste-and-critique.md`](skills/ohmytaste/references/taste-and-critique.md)。

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

构建当前版本独立 ZIP：

```bash
VERSION=$(cat VERSION)
python scripts/package_skill.py --output "dist/ohmytaste-v${VERSION}.zip"
```

## 使用示例

### 宏观领域输入

> 使用 OhMyTaste 调查 mechanistic interpretability 中值得研究的问题。我没有论文清单和已有假设。先比较几个细分方向，再选择一个深入调查，并从文献张力中推导 Proposal。

### 细分方向输入

> 使用 OhMyTaste 调查神经网络 delayed generalization（grokking）。显式记录未解决问题，把最强的机制张力转化为候选假设，独立检索 prior art，并设计能够区分竞争机制的最小实验。

### 允许拒绝推荐

> 调查 RAG evaluation。如果初始候选都被否决，执行一次 residual opportunity recovery。若仍没有足够可靠的机制级 Idea，请输出 `NO RECOMMENDATION`。

## 架构

```text
ohmytaste-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── VERSION
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
└── .github/workflows/
    ├── ci.yml
    └── release.yml
```

按照 Agent Skills 规范，Skill 目录名需要与 `SKILL.md` frontmatter 中的 `name` 保持一致，因此安装名 `ohmytaste` 对应 `skills/ohmytaste/`。

## 局限性

- 无法保证绝对新颖性。数据库覆盖、付费墙、索引延迟和未公开工作都可能造成 prior art 漏检。
- 对论文全文不可访问时，只能标记为 `abstract-only`，不能据此声称核查了具体实验、图表、附录或推导。
- abstract-only 的高度相似可以构成强 collision risk，但在关键创新维度不可见时，不应自动等同于完整科学贡献已经重复。
- 工作流结构本身不能证明 Research Taste 已达到专家水平，仍需要真实案例 Benchmark 和领域研究者盲评。
- 用户未提供算力、数据权限、实验设备或时间预算时，对应资源必须记为 `Unknown`。
- 科学问题可以仍然开放，但由于贡献天花板、竞争、成本或归属风险而被 `DEPRIORITIZE`。

## 开发

运行结构检查和单元测试：

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```

生成确定性 ZIP：

```bash
VERSION=$(cat VERSION)
python scripts/package_skill.py --output "dist/ohmytaste-v${VERSION}.zip"
```

从本地仓库验证 skills CLI 发现：

```bash
npx skills add . --list
```

CI 会执行仓库结构验证、单元测试、ZIP 打包、skills CLI 发现测试和非交互安装 smoke test。若 CI 环境存在 XeLaTeX，还会编译 LaTeX Proposal 模板。

评测案例见 [`evals/test-cases.md`](evals/test-cases.md)。当前包含 12 个 specification-style cases，其中 9–12 专门用于防止真实研究测试中发现的“过度保守、只会否决”的回归。除非未来确实完成人工专家评审并留下记录，项目不会声称已经完成该类评审。

## 贡献

欢迎提交能够提高证据质量、研究机会发现、可证伪性、可复现性或评测覆盖率的修改。工作流变更应增加或更新对应评测案例；检索和证据规则变更应说明所针对的具体失败模式。

请避免仅为了显得复杂而引入框架、评分系统或额外 Agent。

## 许可证

MIT License，详见 [`LICENSE`](LICENSE)。
