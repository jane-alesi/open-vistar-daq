# Tasks: Frontend Integration Testing

**Input**: Design documents from `specs/002-frontend-integration-testing/`

## Phase 1: Setup

- [ ] T001 [P] Configure `frontend/package.json` with `test` and `test:ui` scripts
- [ ] T002 Create `frontend/src/tests/setup.ts` with `import '@testing-library/jest-dom'`
- [ ] T003 Configure `frontend/vite.config.ts` to support Vitest (environment: 'jsdom', setupFiles: './src/tests/setup.ts')

## Phase 2: User Story 1 - Dashboard Presence (P1)

- [ ] T004 [P] [US1] Create failing integration test in `frontend/src/tests/integration/App.test.tsx`
- [ ] T005 [US1] Update `frontend/src/App.tsx` with "Open Vistar DAQ" title to pass the test
- [ ] T006 [P] [US1] Add test for visualization container presence in `frontend/src/tests/integration/App.test.tsx`
- [ ] T007 [US1] Implement placeholder visualization container in `frontend/src/App.tsx`

## Phase 3: Finalization

- [ ] T008 [P] Verify all frontend tests pass with `npm test`
- [ ] T009 Update the main project task list in `specs/001-open-vistar-daq/tasks.md`
