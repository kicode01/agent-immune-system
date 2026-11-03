# agent-immune-system

Evolutionary genetic jailbreak fuzzer and AST tool execution firewall for AI coding agents. Protects agents with shell, SQL, or filesystem privileges against prompt injections and privilege escalation.

[![Genetic Fuzzer](https://img.shields.io/badge/Fuzzing-Multi--Gen%20Genetic-ef4444.svg)](scripts/fuzzer_engine.py)
[![AST Firewall](https://img.shields.io/badge/Firewall-Deterministic%20AST-0284c7.svg)](templates/tool_guard_template.py)
[![Agent Ready](https://img.shields.io/badge/Agent-Antigravity%20%7C%20Claude%20%7C%20Cursor-8b5cf6.svg)](SKILL.md)
[![License](https://img.shields.io/badge/License-MIT-10b981.svg)](LICENSE)

<br/>

![Architecture](./assets/architecture.svg)

---

## Why this exists

Prompt-level guardrails and system prompt instructions can be bypassed by multi-turn gaslighting, Unicode homoglyphs, invisible zero-width characters, or markdown polyglots. When an agent is granted terminal execution or SQL privileges, prompt injection is equivalent to Arbitrary Code Execution (RCE).

`agent-immune-system` enforces a defense-in-depth model:
1. **Adversarial Genetic Fuzzing:** An evolutionary fuzzer mutates attack vectors across generations to uncover vulnerable prompt surfaces.
2. **Deterministic Invariant Membrane:** An AST-level firewall outside the LLM context intercepts and blocks dangerous commands (`rm -rf`, `DROP TABLE`, path traversal) before they reach the OS or database.

---

## Tool Firewall Invariants

* **Shell Tokenization:** Parsed via `shlex` into distinct binary and argument tokens. Blocks metacharacter pipe smuggling (`&&`, `||`, `;`, `$()`) pointing to dangerous binaries.
* **SQL Parsing:** Restricts agent queries to safe `SELECT` operations. Blocks `DROP`, `TRUNCATE`, `ALTER`, and inline comment injections (`--`, `/*`).
* **Sandbox Boundaries:** Blocks file reads/writes outside designated project directories.

---

## Quickstart

Run the evolutionary genetic jailbreak fuzzer to observe attack mutations:

```bash
python scripts/fuzzer_engine.py --demo
```

---

## Installation

### Claude Code — plugin marketplace (recommended)
```bash
/plugin marketplace add kicode01/agent-immune-system
/plugin install agent-immune-system@kicode01
```

### Claude Code — manual
```bash
git clone https://github.com/kicode01/agent-immune-system.git
cp -r agent-immune-system ~/.claude/skills/agent-immune-system      # Personal (all projects)
# or per-project:
cp -r agent-immune-system .claude/skills/agent-immune-system
```

### Claude.ai / Claude Desktop
Run `python tools/package_skill.py` to generate `dist/agent-immune-system.zip`, then upload it under **Settings → Capabilities → Skills**.

### Gemini CLI, Antigravity, Codex CLI and Other Agents
This skill adheres to the open **Agent Skills format** (a folder containing `SKILL.md` with standard YAML frontmatter and runnable scripts):

```bash
git clone https://github.com/kicode01/agent-immune-system.git
```

| Agent | Personal (All Projects) | Per-Project |
| :--- | :--- | :--- |
| **Gemini CLI / Antigravity** | `~/.gemini/skills/agent-immune-system` (or `~/.gemini/config/skills/`) | `.agents/skills/agent-immune-system` |
| **Codex CLI** | `~/.codex/skills/agent-immune-system` | `.codex/skills/agent-immune-system` |
| **Claude Code** | `~/.claude/skills/agent-immune-system` | `.claude/skills/agent-immune-system` |
| **Cursor / Windsurf / Copilot** | See your agent's skills docs | `.cursorrules` or `skills/agent-immune-system` |

```bash
# Gemini CLI & Antigravity
cp -r agent-immune-system ~/.gemini/config/skills/agent-immune-system

# Codex CLI
cp -r agent-immune-system ~/.codex/skills/agent-immune-system
```

---

## Author
Created and maintained by **[Kian](https://github.com/kicode01)**.

---

## Repository Structure

* [`SKILL.md`](./SKILL.md): Comprehensive agent hardening runbook.
* [`scripts/fuzzer_engine.py`](./scripts/fuzzer_engine.py): Multi-generation genetic algorithm fuzzer.
* [`templates/tool_guard_template.py`](./templates/tool_guard_template.py): Deterministic AST-level tool execution membrane.
* [`tools/package_skill.py`](./tools/package_skill.py): Standalone `.zip` packager for Claude Desktop and releases.
* [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json): Claude Code plugin marketplace manifest.
* [`assets/architecture.svg`](./assets/architecture.svg): Security architecture diagram.
