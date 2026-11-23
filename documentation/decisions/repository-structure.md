# Repository Structure Decision

**Date:** 2026-11-24  
**Decision:** Organize learning code by curriculum phase, week, and session.

## Rationale

The previous tree mixed a few Week 2 files at the repository root, used inconsistent capitalization for Week 1 session folders, and grouped some Week 1 exercises in a folder that did not reflect their actual session.

## Conventions

- Keep learning exercises under `phase-XX-topic/week-XX/session-XX/` or a documented week-level `session/` folder where several small exercises belong together.
- Use lowercase names and zero-padded session numbers.
- Give scripts descriptive names; avoid generic root-level names such as `test.py`.
- Keep reports, learning journals, security notes, and technical decisions under `documentation/`.
- Do not commit generated datasets, PCAP files, virtual environments, secrets, or assessed CS50P solutions.

## Moves made

- Put the first security-event script in Week 1 Session 1.
- Normalized the Week 1 Session 2 directory to lowercase.
- Separated Week 1 alert dictionaries, IP validation/counter exercises, and the interactive CLI into Sessions 3, 4, and 5 respectively.
- Moved the Week 2 loop iterator into the Week 2 session folder.
- Renamed the generic root-level random selection exercise to `random_choice_practice.py`.
- Moved the small Session 3 archive under `documentation/archives/`.
- Removed the empty root-level `viva.py`.

## Public repository boundary

This repository is public. Assessed CS50P problem-set solutions must remain outside it, in the appropriate CS50 submission workflow.
