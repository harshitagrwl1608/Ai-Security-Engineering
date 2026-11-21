# Week 01 — Session 2

## Topics covered

- Text formatting and string cleanup (`strip()` and `lower()`).
- Basic arithmetic and calculating a rate from a count and duration.
- Converting input values from strings to integers with `int()`.
- Comparison operators and threshold checks.
- Formatting output with f-strings.
- Writing reusable functions that accept arguments and return values.
- Importing functions from a separate Python module.

## Five exercises completed

1. **Text formatting:** accepted an event name, removed surrounding whitespace and converted it to lowercase.
2. **Arithmetic:** calculated the average number of failed login attempts per minute.
3. **Type conversion:** converted an input value to an integer and checked its type.
4. **Comparisons:** compared a failed-login count against a threshold.
5. **F-strings:** formatted event details into a readable security-event message.

## Three helper functions created

The `helpers.py` module contains:

- `clean_username(username)` — removes surrounding whitespace and converts the username to lowercase; returns the cleaned string.
- `format_event(event_type, source_ip, username)` — creates and returns a formatted security-event message.
- `failed_login_threshold_exceeded(failed_attempts, threshold=5)` — returns `True` when the failed-attempt count is greater than the threshold, otherwise `False`.

## Concepts I can explain

- `input()` returns text, so numeric input must be converted before arithmetic or numeric comparison.
- `print()` displays a result, whereas `return` sends a value back to the code that called a function.
- A module is a Python file whose functions can be imported into another Python file.
- A returned value can be stored in a variable and reused in a later function call.
- The threshold helper uses `>` rather than `>=`; therefore, a count equal to the threshold does not exceed it.

## Code written / files changed

- Five exercise files under `exercises/`.
- `helpers.py` with three reusable helper functions.
- `use_helpers.py` to import and call the helpers from a separate file.

## Exercises and test results

- Ran all five exercise programs from a fresh terminal.
- Ran `use_helpers.py` from a fresh terminal.
- Confirmed the expected outputs for the test inputs used during the session, including a cleaned username, a formatted event, and a Boolean threshold result.
- The learner reported completing Task D. No execution errors were reported.

## Errors encountered and fixes

- No runtime errors were reported during the final execution checks.
- Code review identified a small improvement: reuse the already-cleaned username when formatting the event instead of asking for the username a second time.
- Use `snake_case` for variable names, and choose a Boolean variable name such as `threshold_exceeded` to make its meaning clear.

## Questions still open

- Practise explaining module imports and the difference between `print()` and `return` without referring to notes.
- Rebuild one helper function from a blank file to check independent understanding.
- Add more deliberate edge-case checks, especially for empty usernames and invalid numeric input, in a later testing session.

## Next session target

Represent synthetic security alerts as dictionaries, store multiple alerts in a list, iterate over them, filter alerts using a condition, and inspect what happens when an expected dictionary key is missing.
