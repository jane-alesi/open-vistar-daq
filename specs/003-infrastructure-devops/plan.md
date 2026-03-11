# Implementation Plan: Infrastructure & DevOps Enhancement (GitHub Edition)

**Branch**: `003-infrastructure-devops` | **Date**: 2026-03-11 | **Spec**: `specs/003-infrastructure-devops/spec.md`

## Summary

This plan covers the hosting of the Open Vistar DAQ project on GitHub, the implementation of GitHub Actions pipelines for code quality and security, the establishment of a branching strategy (GitHub Flow), the configuration of GitHub Copilot support, and the maintenance of local CLI tools.

## Technical Context

**Platform**: GitHub.com
**CI/CD**: GitHub Actions (`.github/workflows/*.yml`)
**Code Quality**: ESLint (Frontend), Ruff/Flake8 (Backend)
**Security**: GitHub CodeQL, Dependency Graph, Secret Scanning
**Branching Strategy**: GitHub Flow (main + short-lived feature branches)
**Tools**: gh, uv, git, npm
**AI Support**: GitHub Copilot (`.github/copilot-instructions.md`)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Library-First**: N/A (DevOps task)
- **CLI Interface**: All DevOps scripts MUST be runnable via CLI.
- **Test-First**: GitHub Actions MUST include test execution.
- **Integration-First**: GitHub Actions MUST run integration tests.
- **Simplicity**: Use standard GitHub Actions for Quality/Security.
- **GitHub-First**: Repository is hosted on GitHub as required.

## Project Structure

### Documentation (this feature)

```text
specs/003-infrastructure-devops/
├── plan.md              # This file
├── spec.md              # Feature specification
└── tasks.md             # Task breakdown
```

### Source Code (repository root)

```text
.github/
├── workflows/           # GitHub Actions configuration
│   ├── quality.yml      # Linting and Tests
│   └── security.yml     # CodeQL and Scanning
└── copilot-instructions.md # Copilot custom instructions
```

## Implementation Strategy

1. **Research**: Identify latest GitHub Actions for Python (uv support) and React (npm).
2. **Design**: Draft `.github/workflows/` with jobs: `lint`, `test`, `security`.
3. **Branching**: Verify GitHub Flow locally and push to GitHub.
4. **GitHub Setup**: Repository created, visibility public, and configure protection rules via `gh`.
5. **Tooling**: Attempt tool updates and document results.
6. **Copilot**: Create custom instructions to improve AI assistance quality.
