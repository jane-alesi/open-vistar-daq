<!--
Version change: 1.0.0 -> 1.1.0
List of modified principles:
- VII. Dual-Licensing Compliance (Expanded)
- VIII. GitHub-First Infrastructure (Added)
Templates requiring updates: ✅ updated
-->
# open-vistar-frontend Constitution

## Core Principles

### I. Library-First
Every feature MUST start as a standalone library. Libraries must be self-contained, independently testable, and documented. This forces modular design and prevents tight coupling.

### II. CLI Interface
All libraries MUST expose their functionality via a CLI. This ensures observability and allows for easy integration and debugging. Interface should support standard I/O (stdin/args to stdout, errors to stderr).

### III. Test-First (NON-NEGOTIABLE)
No production code SHALL be written before a corresponding test exists and fails. TDD is the primary quality gate. Red-Green-Refactor cycle must be strictly followed.

### IV. Integration-First
Real-world testing is prioritized over mocks. Use real databases and services for integration tests whenever feasible. Contracts must be defined and validated through contract tests.

### V. Simplicity
We MUST avoid over-engineering. Max 3 projects/modules per feature. No future-proofing or "just in case" abstractions. YAGNI (You Ain't Gonna Need It) is the default stance.

### VI. Anti-Abstraction
Use framework features directly. Avoid creating thin wrappers around stable libraries or frameworks. Every abstraction must be justified by significant complexity reduction or domain-specific needs.

### VII. Dual-Licensing Compliance
Software MUST adhere to the MIT License. Hardware schematics MUST follow CERN-OHL-W-2.0. All files MUST include appropriate license headers and documentation must clearly distinguish between software and hardware components.

### VIII. GitHub-First Infrastructure
All source code and project management MUST happen on GitHub. We MUST use GitHub Flow for branching (main + feature branches). CI/CD MUST be implemented via GitHub Actions.

## Additional Constraints

### Technology Stack
- Backend: FastAPI (Python)
- Message Broker: Eclipse Mosquitto (MQTT)
- Database: InfluxDB (Time-series)
- Frontend: React with Tailwind CSS
- Visualization: Apache ECharts
- Infrastructure: Docker & Docker Compose
- Testing: PyTest (Backend), Vitest/Playwright (Frontend)
- CI/CD: GitHub Actions (Quality & Security)

## Development Workflow

### Quality Gates
1. Specification approved via `/speckit.specify`.
2. Technical plan approved via `/speckit.plan`.
3. Tasks defined and ordered by dependency via `/speckit.tasks`.
4. Tests written and failing before implementation.
5. All tests green before submission.

## Governance
This constitution supersedes all other development practices in this project. Amendments to these principles require a version bump and documentation of the rationale. All pull requests must verify compliance with these principles.

**Version**: 1.1.0 | **Ratified**: 2026-03-11 | **Last Amended**: 2026-03-11
