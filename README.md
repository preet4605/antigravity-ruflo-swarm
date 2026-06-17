# Antigravity Ruflo Swarm

An advanced, native Swarm Coordinator port for the Antigravity CLI. This package brings multi-agent routing, peer-to-peer delegation, and a 6-phase learning loop natively into the terminal.

> **Attribution:** This project is a native Antigravity port of the original [claude-flow](https://github.com/ruvnet/claude-flow) repository created by ruvnet. 

## 🚀 Features

- **134+ Specialized Domain Agents:** Instantly available native skills including `security-auditor`, `seo-content-writer`, `database-architect`, and many more.
- **Peer-to-Peer Handoff:** The Coordinator yields and allows subagents to use `send_message` to pass data directly down the pipeline, reducing token bottleneck.
- **6-Phase Execution Lifecycle:** Includes `ruflo-memory` integration. The Swarm automatically performs Phase 0 (Learn) prior to planning, and Phase 5 (Remember) upon completion.
- **Dynamic Registry Routing:** A Python builder script compiles all 134+ agents into an index so the Swarm can pick the perfect team for any prompt.

## 🛠️ Modifications from Original
This port diverges from the original `claude-flow` in the following ways tailored for Antigravity:
- Bypassed the native Node.js/TypeScript orchestration layer in favor of Antigravity's direct `invoke_subagent` capabilities.
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
