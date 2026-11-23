# Week 02 Report — Python Control Flow and Collections

**Curriculum:** AI Security Engineer Curriculum v2.2  
**Focus:** Severity classification, iteration, grouping, deduplication, sorting, and processing synthetic security events  
**Status:** Core exercises and CLI v2 implemented; final runtime validation and the Week 1–2 independent gate remain pending.

> Evidence note: This report reflects the committed exercise files and code shared during the study sessions. The learner reported an elapsed-time reading of **0.004098 seconds**. The earlier committed timer started before event generation, so that reading must not be treated as a processing-only benchmark. The timer has now been moved to cover the counting loop only; a fresh local run is needed to record a valid processing-only measurement.

## 1. Objectives planned vs completed

| Objective | Status | Evidence / notes |
|---|---|---|
| Implement a severity classifier | Completed as recorded | `severity_classifier.py` uses learner-selected thresholds: 0–2 low, 3–5 medium, and 6+ high. Negative input handling and boundary tests remain to be added. |
| Practise `for` and `while` iteration | Completed | `log_iterator.py` now reports the two loop results independently instead of combining the counts and dividing by two. |
| Group events by source IP | Completed | `group_by_ip.py` implements dictionary-of-lists grouping. CLI v2 applies the same approach to the 1,000-event dataset. |
| Deduplicate alerts | Completed | `deduplicate_rank.py` converts hashable alert values into tuples, uses a set to remove duplicates, then sorts unique tuples by severity priority and time. |
| Compare loops and list comprehensions | Completed as recorded | `list_comprehension.py` compares a loop and comprehension for high-severity alerts and extracts event names. |
| Generate 1,000 repeatable synthetic events | Implemented | `random_data_generator.py` seeds the pseudo-random generator with 42 and returns 1,000 dictionaries containing event, source IP, and severity. |
| Count event types and failed logins | Implemented | `event_counter.py` counts event categories and failed logins. Its timer now starts after generation and surrounds the counting loop. |
| Measure processing time | Fresh measurement pending | The previously reported 0.004098-second reading included generation under the earlier timer placement. Re-run the updated script and record the new result. |
| Build CLI v2 summary, filtering, sorting and grouping | Implemented; local acceptance run pending | `cli_v2.py` contains the four features. Output is limited to samples and group counts to avoid dumping all 1,000 records. Verify grouping conservation locally. |
| Complete the untrusted-log-input security note | Documented | See `documentation/security/untrusted-log-input.md`. |
| Complete Week 2 report | Completed | This report. |
| Pass the Week 1–2 Sunday gate | Pending | Three unseen problems, a closed-book rebuild, test run, and honest skill assessment remain. |

## 2. Deliverables

- `phase-01-python/week-02/session/severity_classifier.py`
- `phase-01-python/week-02/session/log_iterator.py`
- `phase-01-python/week-02/session/group_by_ip.py`
- `phase-01-python/week-02/session/deduplicate_rank.py`
- `phase-01-python/week-02/session/list_comprehension.py`
- `phase-01-python/week-02/session/random_choice_practice.py`
- `phase-01-python/week-02/session/random_data_generator.py`
- `phase-01-python/week-02/session/event_counter.py`
- `phase-01-python/week-02/session/cli_v2.py`
- `documentation/security/untrusted-log-input.md`

## 3. Concepts practised

- Use a dictionary to map event types or severity labels to counts and priorities.
- Use a set when uniqueness is required and a dictionary of lists when grouping records by a key.
- Convert a dictionary record into a tuple when its values are hashable and it must be stored in a set.
- Use `sorted()` with a key function to define domain-specific ordering.
- Use `random.choice()` to select synthetic event attributes and `random.seed()` to make pseudo-random test data repeatable.
- Use `time.perf_counter()` to measure elapsed time.
- Use `lambda` as a compact sorting key and list comprehensions to build filtered lists.

## 4. Security note

Log files and event fields must be treated as untrusted data. Do not interpret log contents as Python code, deserialize attacker-controlled objects, or pass attacker-controlled text to a shell. The standalone security note lists the unsafe operations and safer alternatives.

## 5. Verification and limitations

- The generator source creates exactly 1,000 event dictionaries and fixes the random seed.
- The CLI source includes summary, filtering, severity sorting, and grouping.
- Verify grouping by checking that the sum of all group lengths equals the original event count.
- Verify filtering for all three accepted severities and for invalid input.
- Verify sorting puts high before medium before low and preserves all records.
- No automated pytest suite for these Week 2 functions is currently committed.
- A processing-time result from the updated timer has not yet been recorded.
- This synthetic in-memory exercise is not a packet-processing or production IDS benchmark.

## 6. Remaining work

1. Run `python phase-01-python/week-02/session/cli_v2.py` locally and record its output and grouping conservation count.
2. Run `python phase-01-python/week-02/session/event_counter.py` locally and record the updated processing-only time.
3. Add focused tests for classifier boundaries, filtering, sort order, grouping conservation, and generator reproducibility.
4. Complete Session 8: solve three unseen problems unaided, rebuild one tool without notes, run the available tests, explain a collection choice, and record honest skill levels.
5. Update this report with exact local command output and actual time spent after verification.

---

**Status discipline:** “Implemented” means the source is present and has been reviewed. It does not mean the code has passed a complete automated test suite or an independent acceptance test.
