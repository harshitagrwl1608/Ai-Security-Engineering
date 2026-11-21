# Week 01 Report — Python Foundations

**Curriculum:** AI Security Engineer Curriculum v2.2  
**Focus:** Python fundamentals applied to security-event data  
**Status:** Practical sessions 1–5 completed; moving to Week 2 practice

## 1. Objectives planned vs completed

| Objective | Status | Evidence / notes |
|---|---|---|
| Set up a local Python workspace and virtual environment | Completed | Created `~/AI-Security-Engineering`, a project `.venv`, and the Week 1 folder structure. |
| Install basic development and security tools | Completed as reported | Installed `pytest`, `pip-audit`, and `bandit`. Keep the scan output if you want it available as evidence. |
| Write and run a first security-event script | Completed | Created and ran `security_event.py` with synthetic event details. |
| Complete five small Python exercises | Completed | Text formatting, arithmetic, type conversion, comparisons, and f-strings. |
| Write reusable helper functions | Completed | Implemented username cleaning, event formatting, and failed-login threshold evaluation in `helpers.py`. |
| Import and reuse helper functions | Completed | Created `use_helpers.py` and used the imported functions together. |
| Represent alerts with dictionaries in a list | Completed | Created five synthetic security alerts with consistent fields. |
| Iterate through and filter alert records | Completed | Printed alert fields and filtered by severity, source IP, and event type. Corrected counter placement so only matching records are counted. |
| Experiment with an incomplete dictionary | Completed | Direct access to a missing `severity` key raised `KeyError`. Discussed `.get()` as a safer alternative. |
| Count IP frequency | Completed | Implemented a dictionary-based IP frequency counter. |
| Validate IPv4 addresses | Completed per learner confirmation | Implemented validation for four octets, digit checks, and the 0–255 range. Several early bugs were identified and corrected. |
| Combine validation and frequency counting | Completed per learner confirmation | Valid IPs are counted; invalid entries are excluded and counted separately. |
| Build a mini security-alert CLI | Completed per learner confirmation | Accepts multiple records, validates source IP and severity, rejects invalid records, and prints severity totals. The final corrected version was not independently re-reviewed. |

## 2. Resources used

- CS50P Lectures 0–2 and their problem sets, completed before this practical catch-up work.
- The AI Security Engineer Curriculum v2.2.
- The Weeks 1–2 Catch-Up Plan.
- Python's built-in string, list, dictionary, and function features.
- Local terminal and VS Code workflow.

## 3. Practical deliverables

- `phase-01-python/week-01/security_event.py`
- `phase-01-python/week-01/session-02/exercises/` — five small exercises
- `phase-01-python/week-01/session-02/helpers.py`
- `phase-01-python/week-01/session-02/use_helpers.py`
- `phase-01-python/week-01/session-03/security_alerts.py`
- `phase-01-python/week-01/session-04/ip_counter.py`
- `phase-01-python/week-01/session-04/ip_validator.py`
- `phase-01-python/week-01/session-04/ip_counter_and_validator.py`
- `phase-01-python/week-01/session-05/alert_cli.py`

Adjust the paths above to match the actual filenames and locations in the local workspace.

## 4. Tests and results

| Test / scenario | Result |
|---|---|
| Five synthetic alerts can be stored and printed | Passed during implementation |
| High-severity filtering | Passed; expected count was 2 for the sample data |
| Filtering by `192.168.1.10` | Passed after correcting the counter placement; expected count was 2 |
| Filtering `Failed Login` events | Passed after correcting the counter placement; expected count was 2 |
| Missing dictionary key | Observed `KeyError: 'severity'` as expected |
| IP frequency counter on the mixed sample list | Expected frequencies: `192.168.1.10: 3`, `10.0.0.5: 2`, `192.168.1.20: 1` |
| Invalid IP handling on the mixed sample list | Expected invalid count: 3 |
| Alert CLI severity summary | Implemented for low, medium, and high; invalid IPs and severities are rejected. Learner reports correcting the final code. |

The sample-data results above are based on the work discussed during the sessions. Save repeatable test inputs and terminal output alongside the code when possible. The final versions of all files and a complete test run were not supplied together for an independent end-to-end audit.

## 5. Concepts I can implement or explain

- Use lists to hold multiple records and dictionaries to represent one structured record.
- Retrieve dictionary values using keys and test key existence with `in`.
- Use `.get()` to provide a default when a dictionary key may be absent.
- Iterate over records with `for` loops and filter them with conditions.
- Count occurrences by using dictionary keys and integer values.
- Split a string into IPv4 octets, validate numeric content, convert octets to integers, and check their ranges.
- Pass lists to functions and return dictionaries or Boolean results.
- Import functions from another Python module.
- Use `if __name__ == "__main__":` to prevent a module's demonstration `main()` function from running automatically when imported.
- Use `continue` to reject an invalid input record and proceed to the next iteration.

## 6. Difficulties and fixes

- A frequency counter was initially incrementing for every item instead of only matching items. The increment was moved inside the matching condition.
- The IPv4 validator initially had an incorrect comparison expression and checked the same octet multiple times. The checks were corrected to validate all four octets independently.
- An incomplete alert caused `KeyError` when the missing key was accessed directly. `.get()` was discussed as an alternative for optional fields.
- A module appeared to execute old code because the editor buffer had not been saved. Saving the current file resolved the stale-code confusion. The `__main__` guard was also learned as a separate way to prevent demonstration code from running during imports.
- The CLI initially assigned the built-in `type` rather than the `severity` variable. The learner reports fixing the final version.

## 7. Security task

- `pip-audit` and `bandit` were installed as part of the environment setup.
- The project uses a `.gitignore` intended to exclude the virtual environment, caches, `.env`, PCAP files, datasets, and model artifacts.
- The output of the security scans and the pinned dependency file should be retained as evidence in the repository.
- The CLI validates IPv4 input and restricts severity to `low`, `medium`, or `high`.

## 8. Time spent

Not recorded accurately. The catch-up plan allocates approximately 2 hours per session; actual time should be entered by the learner rather than estimated after the fact.

## 9. Next priorities

1. Complete Week 2 Session 6: severity classification, loop practice, grouping by source IP, deduplication, and ranking.
2. Test threshold boundary values and document the chosen thresholds.
3. Complete the 1,000-event processor and CLI v2 in Session 7.
4. Complete the independent Week 1–2 gate in Session 8, including three unseen problems and rebuilding one tool from a blank file.
5. Keep CS50P assessment solutions in the existing CS50 submission repository and do not publish them in a public portfolio.

---

**Learner note:** This report records work completed as discussed and the learner's confirmation that the final code issues were fixed. Keep the report honest: append exact test output, actual time spent, and any remaining gaps as you verify them locally.
