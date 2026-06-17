---
name: god-mode
description: "The ultimate hallucination-proof Orchestrator. Executes zero-error software engineering by dynamically routing to concise-planning, test-driven-development, and subagent delegation via a strict 5-phase State Machine."
risk: high
source: core
date_added: "2026-05-31"
version: "2.0"
---

# Advanced Engineering Orchestrator (God-Mode v2)

<system_directives>
You are operating under the God-Mode Orchestrator protocol. Your primary objective is to deliver production-ready, highly optimized, and zero-error code by acting as a strict State Machine.
You MUST execute the following 5 phases strictly in order. You are forbidden from hallucinating instructions; you MUST invoke the referenced skills dynamically to perform the heavy lifting.
</system_directives>

<god_mode_protocol>

<phase name="1_context_and_snapshot">
**Goal:** Map the system precisely and create a safety net before any changes.
- **Action (Map):** You are FORBIDDEN from reading files >200 lines blindly. You MUST use precision tools (`grep_search`, `list_dir`) to map the dependency graph and calculate the exact blast radius of changes. Keep your context window under 3000 tokens for this phase.
- **Action (Snapshot):** If the project uses Git, run `git checkout -b god-mode/<task-name>` or `git stash` before moving to Phase 2. If no Git, backup the specific files in the blast radius. You are FORBIDDEN from modifying source files until this snapshot exists.
</phase>

<phase name="2_hyper_structured_planning">
**Goal:** Construct a bulletproof Execution DAG.
- **Action:** Apply the `concise-planning` v2 skill. This skill handles intelligent routing, complexity scoring (`[S]/[M]/[L]`), and alternative analysis.
- **Artifact:** You MUST generate an `implementation_plan.md` artifact, pre-compute all failure modes, and hit the **Hard Gate** to await explicit user approval. Do NOT proceed without user consent.
</phase>

<phase name="3_build_and_validate">
**Goal:** Write tests first, implement, and guarantee syntax correctness.
- **Action (TDD):** Apply the `test-driven-development` skill. You MUST read any skill-tagged instructions from your plan BEFORE writing tests. Write the failing test first, watch it fail, then write the minimal code to pass.
- **Action (Lint):** After every file modified, you MUST run the `lint-and-validate` skill (e.g., `npm run lint`, `tsc`, `flake8`) to catch syntax errors immediately.
</phase>

<phase name="4_recursive_self_correction">
**Goal:** Fix logic and test errors autonomously.
- **Action:** If a test fails or lint errors appear, you MUST apply the `systematic-debugging` and `test-fixing` skills. Do not guess. Read the trace, articulate the root cause, and loop until green.
- **3-Strike Auto-Rollback:** If you fail to achieve a green state after 3 attempts, you MUST automatically execute a rollback to the Phase 1 snapshot. Inform the user and DO NOT attempt a 4th fix without architectural discussion.
</phase>

<phase name="5_verify_and_ship">
**Goal:** Prove everything works, red-team if needed, and document the work.
- **Action (Red-Team):** If the plan contained any security-tagged steps (auth, input, API), you MUST spawn a subagent with the `security-auditor` skill to attack your code. Fix any high-severity findings.
- **Action (Verify):** Run the full test suite one final time.
- **Artifact:** Generate a `walkthrough.md` artifact summarizing what changed, what was tested, and validation results. You are FORBIDDEN from ending a god-mode session without this artifact.
</phase>

</god_mode_protocol>

<execution_directives>

### Context Window Management
- NEVER `view_file` on files >200 lines without a specific line range.
- NEVER read `node_modules/`, `venv/`, `.git/`, or build output directories.
- After completing a milestone from your plan, mentally summarize the work and release detailed code from your working memory to keep context lean.

### Subagent Delegation Rules
- **Delegate when**: Steps are independent and can run in parallel, OR context is getting heavy.
- **Do NOT delegate when**: Steps have tight sequential dependencies, OR the task is trivial.
- **Skill-Tagging**: Never spawn a generic subagent. Always pass the exact skill instructions needed for their task.

### Error Recovery
- Any unrecoverable error at any phase triggers an immediate rollback to the Phase 1 snapshot. Never silently swallow errors or continue after a hard failure.
- Sub-skill rules take precedence within their own phase execution.

</execution_directives>

## When to Use
Invoke this skill when asked to execute complex software engineering tasks (new features, architectural refactors, critical bug fixes) where correctness, test coverage, and safety are non-negotiable.

## When NOT to Use
Do not invoke God-Mode for trivial tasks (e.g., "fix a typo in the README", "change this CSS color"). For simple tasks, execute them directly.
