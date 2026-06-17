# Antigravity Ruflo Swarm

An advanced, highly-rigid Swarm Coordinator port for the Antigravity CLI. This package brings an **Active Director (Hub & Spoke)** multi-agent orchestration model and a **mandatory 6-phase learning loop** natively into the terminal.

> **Attribution:** This project is a native Antigravity port of the original [claude-flow](https://github.com/ruvnet/claude-flow) repository created by ruvnet. 

## 🚀 Features

- **134+ Specialized Domain Agents:** Instantly available native skills including `security-auditor`, `seo-content-writer`, `database-architect`, and many more.
- **Active Director (Hub & Spoke) Model:** The Main Agent acts strictly as a Director. It cannot execute code or bypass the pipeline; it must assign work to specialized subagents and actively review their outputs.
- **Hierarchical Subagent Spawning:** Subagents are explicitly authorized to use `invoke_subagent` to spawn their own teams if a task becomes too complex.
- **Strict 6-Phase State Machine:** The Coordinator is physically forced to maintain a state file (`ruflo_state.json`) and cannot skip, merge, or bypass any of the 6 phases.
- **Mandatory Self-Improvement:** The protocol enforces a strict Phase 0 (Memory Retrieval) and Phase 5 (Self-Improvement). The task is considered a failure if the AI does not write a permanent post-mortem learning pattern to the disk.
- **Dynamic Registry Routing:** A Python builder script compiles all 134+ agents into an index so the Swarm can pick the perfect team for any prompt.

## 🛠️ Modifications from Original
This port diverges from the original `claude-flow` in the following ways tailored for Antigravity:
- Bypassed the native Node.js/TypeScript orchestration layer in favor of Antigravity's direct `invoke_subagent` capabilities.
- Enforced a strictly monitored **Director-only** model instead of a loose peer-to-peer network.
- Removed the SQLite/WASM memory dependency (which crashes on ARM64 Termux) in favor of semantic `grep_search` against a local Markdown knowledge bank.

## 📥 Installation

The fastest way to install the Swarm Coordinator and all 134+ agents into your Antigravity environment is to run this single command in your terminal:

```bash
git clone https://github.com/preet4605/antigravity-ruflo-swarm.git /tmp/ruflo-swarm && cd /tmp/ruflo-swarm && chmod +x setup.sh && ./setup.sh && rm -rf /tmp/ruflo-swarm
```

### Manual Installation
If you prefer to review the code first:
```bash
git clone https://github.com/preet4605/antigravity-ruflo-swarm.git
cd antigravity-ruflo-swarm
chmod +x setup.sh
./setup.sh
```

## ⚙️ Configuration
No API keys are required beyond what your Antigravity CLI already uses. If you wish to configure memory paths, you can create a `.env.example` to map `$MEMORY_DIR` if you alter the defaults.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

**Disclaimer:** The software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
