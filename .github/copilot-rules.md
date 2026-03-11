# GitHub Copilot Rules for Open Vistar DAQ

# High-level goals
- Quality and Security are non-negotiable.
- Consistency with the Spec-Driven Development (SDD) workflow.

# Quality checks
- Always suggest tests before implementation when a new feature is requested.
- Prefer Python 3.13 features (type hinting, performance).
- Ensure TypeScript strict mode is followed in Frontend.

# Exclusions
- Do not suggest changes to the `.specify/memory/` directory unless explicitly asked, as it contains project immutable principles.
- Ignore `node_modules` and `.venv`.

# Context Engineering
- Refer to `specs/` for feature requirements.
- Use `backend/src/models/events.py` as the primary reference for DAQ data structures.
