# Handling Untrusted Log Input

**Scope:** Python utilities that ingest logs, alerts, or records from external sources.

Treat every field read from a log as untrusted data. A log line may be malformed or deliberately crafted by an attacker. Parsing should convert input into a constrained representation; it must not execute or deserialize the content as code.

## Operations never to apply directly to untrusted log content

| Operation | Why it is unsafe | Safer approach |
|---|---|---|
| `eval(log_text)` | Evaluates text as a Python expression and may execute attacker-controlled code. | Parse a defined data format with a constrained parser; validate resulting types and fields. |
| `exec(log_text)` | Executes arbitrary Python statements supplied as text. | Never execute log content. Treat it strictly as data. |
| `pickle.loads(log_bytes)` | Unpickling untrusted data can execute code during object reconstruction. | Prefer JSON or another non-executable interchange format, then validate the schema and values. |
| `os.system(log_text)` | Sends a command string to a shell; attacker-controlled text can alter the command. | Avoid shell execution. When a subprocess is genuinely needed, pass a fixed executable and an argument list, never build a shell command from log fields. |
| `subprocess.run(..., shell=True)` with log-derived text | Shell metacharacters and substitutions can turn data into commands. | Use a fixed argument array with `shell=False`, validate arguments, and apply least privilege. |
| Unsafe YAML loading / custom YAML constructors | YAML loaders configured to construct arbitrary Python objects can perform unsafe object construction. | Use `yaml.safe_load` for untrusted YAML, then validate the structure and impose size/depth limits. |

## Defensive parsing practices

- Parse into plain strings, numbers, lists, and dictionaries.
- Validate required keys, allowed event names, severity values, IP address syntax, and field types.
- Apply limits to input size, line length, number of records, and nesting depth where relevant.
- Keep malformed records and rejection reasons observable; do not silently discard data.
- Escape or sanitize untrusted values before displaying them in terminals, HTML, or reports.
- Avoid logging secrets and credentials.
- Keep file access constrained to an intended data directory; do not trust paths supplied by log content.
- Do not treat a regular-expression shape match as proof that a value is semantically valid.

## Core rule

**Logs are evidence, not instructions.** Never interpret log content as executable code, a shell command, or an object-serialization stream.
