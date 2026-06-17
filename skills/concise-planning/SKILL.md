---
name: concise-planning
description: "Intelligent planning engine with skill routing, complexity estimation, and DAG sequencing. Turns user requests into actionable, skill-tagged execution plans with pre-computed failure modes."
risk: high
source: core
date_added: "2026-05-31"
version: "2.0"
---

# Concise Planning v2 (God-Level)

## Goal
Turn a user request into an **actionable, persistent artifact** mapped out as a Directed Acyclic Graph (DAG) with intelligent skill routing, complexity scoring, and pre-computed failure modes.

---

## Workflow (8 Phases — Strict Sequential Order)

### Phase 1: Deep Context Scan
- Use `grep_search` and `list_dir` to map the project structure. Do NOT blindly read massive files.
- Identify: language, framework, package manager, test runner, CI config.
- Calculate **blast radius**: how many files/modules will be touched?
- **RULE**: If blast radius > 10 files, flag as high-complexity and include a global rollback strategy.

### Phase 2: Information Freshness Verification
- You MUST explicitly search the live web (via `search_web` or a `research` subagent) to verify the latest documentation, API structures, or architecture patterns related to the task.
- You are **FORBIDDEN** from relying solely on internal training data for third-party libraries, APIs, or external system integrations.
- Only proceed once you have confirmed the freshness of your technical assumptions.

### Phase 3: Codebase Pattern Detection
- Before proposing *how* to build something, check *how the codebase already does it*.
- Search for: naming conventions, folder structure, state management, API style, error handling patterns, test patterns.
- **RULE**: Your plan MUST conform to existing codebase conventions unless the user explicitly requests a refactor.

### Phase 4: Intelligent Skill Routing
- Scan `~/.agents/skills/` at runtime via `list_dir` to discover the actual available skill set.
- For each planned step, score available skills by relevance using these rules:

1. **Keyword Match** — Extract action verbs and domain nouns from the step. Match against skill names and descriptions.
2. **Cluster Narrowing** — Identify which domain cluster(s) the task falls into. Prioritize skills within matching clusters.
3. **Multi-Skill Stacking** — A single step CAN be tagged with multiple skills if the work spans domains (e.g., `[frontend-developer, premium-frontend-ui]`).
4. **Specificity Over Generality** — Always prefer a narrow, specialized skill over a broad one. Example: `react-native-architecture` over `mobile-developer` for React Native navigation.
5. **Security Auto-Inject** — If ANY step touches authentication, user input, API endpoints, or data storage, you MUST auto-inject a security skill as a secondary tag even if the user didn't ask for it.

- **RULE**: Every DAG step MUST have at least one `[skill-tag]`. Untagged steps are FORBIDDEN.

#### Skill Domain Clusters (Quick Reference)

| Cluster | Skills |
|---------|--------|
| **Frontend/Web** | `frontend-developer`, `frontend-design`, `react-patterns`, `react-best-practices`, `nextjs-best-practices`, `nextjs-app-router-patterns`, `tailwind-patterns`, `premium-frontend-ui`, `high-end-visual-design`, `gsap-framer-scroll-animation`, `scroll-experience`, `3d-web-experience`, `web-design-reviewer` |
| **Mobile** | `mobile-developer`, `mobile-design`, `react-native-architecture`, `expo-*`, `flutter-expert`, `android-jetpack-compose-expert`, `android_ui_verification`, `ios-developer`, `swiftui-*` |
| **Backend** | `backend-dev-guidelines`, `python-fastapi-development`, `async-python-patterns`, `api-patterns`, `database-design`, `database-architect`, `stripe-integration` |
| **Security** | `security-auditor`, `vulnerability-scanner`, `api-security-best-practices`, `backend-security-coder`, `frontend-security-coder`, `mobile-security-coder`, `frontend-mobile-security-xss-scan`, `cc-skill-security-review`, `top-web-vulnerabilities`, `auth-implementation-patterns`, `cloud-penetration-testing`, `pci-compliance` |
| **Testing** | `test-driven-development`, `test-fixing`, `e2e-testing-patterns`, `systematic-debugging`, `lint-and-validate` |
| **Design/UX** | `ui-ux-pro-max`, `high-end-visual-design`, `canvas-design`, `mobile-design`, `interactive-portfolio`, `form-cro`, `seo-audit` |
| **DevOps** | `git-pushing`, `expo-cicd-workflows`, `expo-deployment`, `performance-optimizer` |
| **Architecture** | `architecture-blueprint-generator`, `graphify`, `code-review-checklist`, `kaizen`, `senior-fullstack` |
| **Games** | `game-engine`, `slang-shader-engineer` |
| **AI/ML** | `computer-vision-expert`, `local-llm-expert` |
| **Content** | `content-creator`, `copy-editing`, `ab-test-setup`, `algorithmic-art` |

> **NOTE**: This table is a fast-path heuristic. Always `list_dir ~/.agents/skills/` at runtime to discover newly added skills not yet in this table.

### Phase 5: Complexity Estimation
- Assign each step a complexity score:
  - `[S]` **Simple** — Single file, <30 min, low risk.
  - `[M]` **Medium** — 2-5 files, 1-2 hours, moderate risk.
  - `[L]` **Large** — 5+ files, half-day+, high risk, needs snapshot.
- Sum scores for an **overall complexity estimate**.
- **RULE**: If ANY step is `[L]`, the plan MUST include a Global Rollback Strategy (git branch or stash before execution begins).

### Phase 6: Alternatives Analysis
- For any non-trivial architectural or technology decision, briefly document at least 2 approaches.
- State which one you chose and *why* (tradeoff reasoning).
- **RULE**: This section is OPTIONAL for plans where ALL steps are `[S]` complexity. MANDATORY for plans containing `[M]` or `[L]` steps.

### Phase 7: Minimal Interaction
- Ask **at most 1–2 questions** and only if truly blocking.
- Make reasonable assumptions for non-blocking unknowns.

### Phase 8: Generate Artifact & Hard Gate
- You are **FORBIDDEN** from printing the plan into the chat UI.
- You MUST use `write_to_file` to generate an `implementation_plan.md` artifact.
- You MUST set `RequestFeedback=true` in the tool call.
- After generating the artifact, you MUST **STOP** and await explicit user approval. Do not write implementation code until confirmed.

---

## Artifact Template

Your `implementation_plan.md` MUST follow this structure:

```markdown
# Execution Plan: [Title]

**Approach**: 1-3 sentences on what and why.

**Overall Complexity**: [S/M/L] — Estimated [time]. Blast radius: [N files].

## Scope
- **In Scope**:
- **Out of Scope**:

## Alternatives Considered
_(OPTIONAL for all-[S] plans. MANDATORY for [M]/[L] plans.)_

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| A: [approach] | ... | ... | **Selected** |
| B: [approach] | ... | ... | Rejected because... |

## Codebase Conventions Detected
- **Naming**: [e.g., camelCase components, snake_case utils]
- **State Management**: [e.g., Zustand, Redux, Context]
- **API Style**: [e.g., REST with Express, tRPC]
- **Test Runner**: [e.g., Jest, Vitest, pytest]

## Global Rollback Strategy
_(MANDATORY if any step is [L]. RECOMMENDED otherwise.)_

> Before executing Step 1, create a safety snapshot:
> `git checkout -b feature/plan-name` or `git stash`

## Execution DAG (Action Items)

### Milestone 1: [Foundation]
- [ ] **Step 1 `[S]` [skill-tag]:** <Atomic Action>
- [ ] **Step 2 `[M]` [skill-tag-1, skill-tag-2]:** <Dependent Action>

### Milestone 2: [Core Feature]
- [ ] **Step 3 `[L]` [skill-tag]:** <Action> ⚠️ SNAPSHOT REQUIRED

## Pre-Computed Failure Modes
- **Step X Failure Risk:** <What could go wrong>
  - **Mitigation/Rollback:** <How to fix or revert>

## Subagent Delegation Strategy
_(OPTIONAL for all-[S] plans. MANDATORY for [M]/[L] plans.)_

| Step(s) | Strategy | Reason |
|---------|----------|--------|
| 1, 2 | Sequential (self) | Dependencies between steps |
| 3, 4 | Parallel subagents | Independent, can run concurrently |
| 5 | Research subagent | Web lookup, non-blocking |

## Validation Strategy
- <Exact command or manual test to prove success>

## Open Questions
- <Question 1 (max 2)>
```

---

## Checklist Guidelines

- **Atomic**: Each step is a single logical unit of work.
- **Verb-first**: "Add...", "Refactor...", "Verify...".
- **DAG Sequenced**: Never list tasks out of dependency order.
- **Skill-Tagged**: Every step MUST have at least one `[skill-tag]`. Untagged steps are FORBIDDEN.
- **Complexity-Scored**: Every step MUST have a `[S]`/`[M]`/`[L]` score.
- **Security Auto-Inject**: Steps touching auth/input/APIs MUST have a security skill tag.
- **Pattern-Conformant**: Plans MUST respect existing codebase conventions unless explicitly asked to refactor.
- **Milestone-Grouped**: For plans with 5+ steps, group steps into logical milestones.

## When to Use
Invoke this skill whenever a user requests a plan, roadmap, or before beginning any high-complexity execution that warrants structural review.
