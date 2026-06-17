---
name: ruflo-memory
description: "Native Antigravity port of the Ruflo adaptive memory system. Use this skill when executing the Phase 5 Learning Loop of a swarm task, or when retrieving past patterns at the start of a task."
---

# Ruflo Adaptive Memory (Antigravity Native)

You are operating the Ruflo Self-Learning Loop. Instead of a native vector database, you use Antigravity's file-based storage and `grep_search` to achieve semantic retrieval and persistence.

## The Memory Bank Structure
All memory is stored in `~/.agents/memory/learnings/`. It is split into two scopes:
1. **Global (`global/`):** Universal technical lessons, general debugging strategies, language/framework best practices.
2. **Contextual (`<project_hash>/`):** Business logic, proprietary API rules, and architecture specific to the current codebase. (Use a simple base64 or md5 hash of the current working directory path as the folder name).

Inside these folders, memories are further grouped into namespaces:
- `patterns/`: Successful architectural or code patterns.
- `feedback/`: Edge cases, errors encountered, and how they were fixed.
- `solutions/`: Reusable code snippets or commands.

## The 4-Step Canonical Loop

### 1. RETRIEVE (Start of Task)
Before writing code for a new task, use `grep_search` to scan the `learnings/global/` and `learnings/<current_project_hash>/` directories.
- Search for 1-3 keywords relevant to the user's prompt (e.g., "auth", "database", "react").
- Read any matched files and inject their lessons into the Architect and Coder subagent prompts.

### 2. JUDGE (During Task)
Monitor the Coder and Reviewer. Note what attempts fail and what solutions finally pass the tests. 

### 3. DISTILL (End of Task)
Once the task is verified (Phase 4 of Swarm), run a post-mortem:
- What worked? What failed?
- Distill the findings into concise Markdown snippets.
- Tag each snippet with 2-3 relevant `#hashtags` so `grep_search` can find it easily later.

### 4. CONSOLIDATE (Saving State)
Determine the scope of the distilled knowledge:
- Does this apply to *any* project using this language? -> Save to `global/`.
- Is this specific to this app's database or business rules? -> Save to `<current_project_hash>/`.

Use `write_to_file` to save the Markdown snippet. 
- Filename format: `[namespace]_[timestamp]_[keywords].md` (e.g., `feedback_1718542_auth_token.md`).

## Memory Pruning
If a search returns more than 10 files for a single keyword, flag it. In a future task, you will need to spawn a `researcher` to consolidate those 10 granular files into one dense `MASTER_[keyword].md` file to prevent context window bloat.
