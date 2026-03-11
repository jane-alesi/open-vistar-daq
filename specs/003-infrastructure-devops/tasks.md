---

description: "Task list template for feature implementation"
---

# Tasks: Infrastructure & DevOps Enhancement

**Input**: Design documents from `specs/003-infrastructure-devops/`
**Prerequisites**: `plan.md`, `spec.md`

## Phase 1: Setup (GitLab Initialization)

- [ ] T001 [P] Create public GitLab repository `open-vistar-daq` under `jane-alesi`
- [ ] T002 Add GitLab remote to local repository (`git remote add gitlab https://gitlab.com/jane-alesi/open-vistar-daq.git`)
- [ ] T003 Initialize GitFlow branching model (`main`, `develop`)

## Phase 2: CI/CD Implementation

- [ ] T004 Create root `.gitlab-ci.yml` with basic stages (`lint`, `test`, `security`)
- [ ] T005 Implement `backend-test` job in `.gitlab-ci.yml` (using `pytest`)
- [ ] T006 Implement `frontend-test` job in `.gitlab-ci.yml` (using `npm test`)
- [ ] T007 [P] Add GitLab SAST template to `.gitlab-ci.yml`
- [ ] T008 [P] Add Secret Detection template to `.gitlab-ci.yml`

## Phase 3: Tooling & Best Practices

- [ ] T009 Attempt update of CLI tools (gh, glab, uv) and document current versions
- [ ] T010 Configure GitLab branch protection rules for `main` and `develop`
- [ ] T011 Document GitFlow usage in `README.md`

## Phase 4: Final Migration

- [ ] T012 Push all branches to GitLab (`git push gitlab --all`)
- [ ] T013 Verify pipeline execution on GitLab
- [ ] T014 Ensure GitHub remote is also updated or maintained as mirror
