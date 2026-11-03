---
name: agent-immune-system
description: >-
  [WHAT IT DOES]: Protects AI agents with real-world tool execution rights (shell commands, SQL queries, API writes)
  against prompt injections, indirect jailbreaks, and privilege escalation using evolutionary genetic fuzzing and AST tool membranes.
  [WHEN TO USE]: Use when building autonomous agents that execute terminal commands, modify databases, parse untrusted
  external documents (PDFs, scraped HTML, customer emails), or run in sensitive enterprise environments.
  [WHEN NOT TO USE]: Do NOT use for basic read-only conversational chatbots without tool-calling or execution privileges.
---

# Agent Immune System: Adversarial Jailbreak Fuzzer & Tool Membrane

```
  +---------------------------------------------------------------------------------+
  |                             AGENT IMMUNE SYSTEM                                 |
  |         Evolutionary Genetic Jailbreak Fuzzer & Tool AST Firewall               |
  +---------------------------------------------------------------------------------+

  [Untrusted External Data / User Prompt]
  (Scraped HTML, User Uploads, Webhooks, Emails)
                        |
                        v
         [LLM Cognitive Intent Processor]
         - System Prompt Context Window
         - Vulnerable to Semantic Gaslighting & Hijacking
                        |
                        v
          [Proposed Tool Execution Call]
          - E.g.: `bash("rm -rf /")` or `sql("DROP TABLE")`
                        |
                        v
   +-------------------------------------------------------+
   |           DETERMINISTIC INVARIANT MEMBRANE            |
   |              (Outside the LLM Context)                |
   |  - AST Shell Tokenizer & Invariant Whitelist          |
   |  - SQL Parser Blocking DDL & Dangerous Mutations      |
   |  - Path Chroot & Network Egress Boundary Checks       |
   +-------------------------------------------------------+
                        |
        +---------------+---------------+
        |                               |
  [Invariant Passes]             [Invariant Breached]
        v                               v
  [Execute Tool Safely]          [Execution Denied]
                                 - Log Attack Geometry
                                 - Trigger Evolutionary Fuzzer
                                 - Auto-Patch Defense Membrane
```

---

## 1. When to Activate

Trigger `agent-immune-system` when:
- **Authorizing Agent Tool Execution:** Granting an agent shell execution, file system modifications, or database write access.
- **Processing Untrusted Inputs:** Ingesting external web scrapes, user-uploaded resumes, emails, or third-party webhooks that could contain hidden instructions.
- **Enterprise Red-Teaming:** Performing automated penetration testing on agent swarms before deploying them to customers.
- **Defense-in-Depth:** Ensuring that even if an attacker completely compromises the LLM prompt, the agent *physically cannot execute malicious actions* at the runtime boundary.

---

## 2. Hardening Runbook

### Step 1: Run the Genetic Adversarial Fuzzer
Launch the multi-generational fuzzer to explore bypass geometries:
```bash
python scripts/fuzzer_engine.py --demo
```
The fuzzer mutates attack vectors across multiple families:
1. **Steganographic Injections:** Zero-width Unicode characters (`\u200b`) separating malicious tokens.
2. **Homoglyph Substitutions:** Replacing Latin letters with identical-looking Cyrillic glyphs to bypass regex filters.
3. **Encoding Smugglers:** Base64, rot13, and URL-encoded execution directives.
4. **Markdown Polyglots:** Hidden HTML comments (`<!-- override -->`) and code block breakouts.

### Step 2: Implement the Deterministic Invariant Membrane
Wrap all agent tool handlers using the template in [tool_guard_template.py](./templates/tool_guard_template.py):
```python
from templates.tool_guard_template import validate_shell_execution, validate_sql_query

def safe_shell_tool(command: str):
    # Deterministic AST validation occurs BEFORE subprocess invocation
    validate_shell_execution(command)
    return subprocess.run(command, shell=True)
```

### Step 3: Enforce Execution Invariants
- **Filesystem Chroot:** Disallow any tool call navigating outside the designated project sandbox root.
- **SQL Parsing:** Restrict agent queries to strictly read-only parameterized `SELECT` queries unless explicit mutation permission is granted for a specific table.
- **Zero-Egress Network Isolation:** Block unauthorized external outbound IP connections.

---

## 3. Reference Files
- [fuzzer_engine.py](./scripts/fuzzer_engine.py): Genetic algorithm fuzzer for testing prompt injection resilience.
- [tool_guard_template.py](./templates/tool_guard_template.py): AST-level tool execution membrane and validator.
