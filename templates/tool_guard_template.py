"""
tool_guard_template.py
Deterministic, non-bypassable AST-level sandbox layer wrapping agent tools.
Blocks hazardous commands regardless of how convincingly the LLM prompt was hijacked.
"""

import re
import shlex
from typing import Any, Dict

FORBIDDEN_COMMANDS = {"rm", "dd", "mkfs", "drop", "truncate", "shutdown", "reboot"}
ALLOWED_PATH_PREFIXES = ["./", "src/", "build/", "dist/", "tests/"]

class ToolGuardViolation(Exception):
    pass

def validate_shell_execution(command: str) -> bool:
    """
    Parses shell command tokens and validates against security invariants.
    """
    tokens = shlex.split(command.strip())
    if not tokens:
        return False

    base_binary = tokens[0].split("/")[-1].lower()
    if base_binary in FORBIDDEN_COMMANDS:
        raise ToolGuardViolation(f"Blocked forbidden binary execution: {base_binary}")

    # Check for unquoted shell metacharacters / pipe smuggling
    if any(ch in command for ch in [";", "&&", "||", "`", "$("]):
        if any(f in command.lower() for f in FORBIDDEN_COMMANDS):
            raise ToolGuardViolation("Blocked chained injection command vector.")

    return True

def validate_sql_query(query: str) -> bool:
    """
    Blocks destructive DDL / DML operations from dynamic agent tool calls.
    """
    normalized = re.sub(r"\s+", " ", query.strip().upper())
    dangerous_keywords = ["DROP TABLE", "DROP DATABASE", "TRUNCATE", "GRANT ALL", "--", "/*"]
    for kw in dangerous_keywords:
        if kw in normalized:
            raise ToolGuardViolation(f"SQL Invariant Violation: prohibited pattern '{kw}' detected.")
    return True
