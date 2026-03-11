# Tasks: Infrastructure & DevOps Enhancement (GitHub Edition)

**Input**: Design documents from `specs/003-infrastructure-devops/`
**Prerequisites**: `plan.md`, `spec.md`

## Phase 1: Setup (GitHub Initialization)

- [X] T001 [P] Create public GitHub repository `open-vistar-daq` under `jane-alesi`
- [X] T002 Add GitHub remote `origin` and push scaffold
- [X] T003 Initialize GitHub Flow branching model (main + feature branches)

## Phase 2: CI/CD Implementation (GitHub Actions)

- [X] T004 Create `.github/workflows/quality.yml` with jobs (`lint`, `test`)
- [X] T005 Implement `backend-test` job in `quality.yml` (using `uv` and `pytest`)
- [X] T006 Implement `frontend-test` job in `quality.yml` (using `npm test`)
- [X] T007 Create `.github/workflows/security.yml` with CodeQL analysis
- [X] T008 [P] Enable Secret Scanning and Dependabot in GitHub settings

## Phase 3: AI Support & Best Practices

- [X] T009 Create `.github/copilot-instructions.md` for project context
- [X] T010 Configure GitHub branch protection rules for `main`
- [X] T011 Document GitHub Flow usage in `README.md`
- [X] T012 Attempt update of CLI tools (gh, uv) and document current versions

## Phase 4: Verification

- [ ] T013 Verify GitHub Actions execution on GitHub
- [ ] T014 Run all local tests to ensure consistency with CI
