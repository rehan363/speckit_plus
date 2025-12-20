# Tasks: World-Class Calculator

**Feature**: World-Class Calculator
**Branch**: `001-simple-calculator-spec`

## Implementation Strategy

The implementation will be phased to deliver value incrementally, starting with a robust, test-driven core logic engine, followed by the UI.

1.  **MVP Scope (Phase 1-2)**: A fully functional, command-line accessible calculator engine that handles basic arithmetic, order of operations, and error handling. This will be the foundation for the UI.
2.  **UI Development (Phase 3-4)**: Build the PyQt user interface and integrate it with the core engine.
3.  **Final Polish (Phase 5)**: Refine the UI, add themes, and ensure a polished user experience.

## Dependencies

-   **US1, US2, US3 (Core Logic)** are foundational and must be completed before the UI.
-   **UI Phase** depends on the completion of the Core Logic phase.

## Phase 1: Project Setup

-   [X] T001 Create the project directory structure (`src/calculator`, `tests`).
-   [X] T002 Initialize the `pyproject.toml` file with project metadata and dependencies (`pytest`, `ruff`, `mypy`, `PyQt6`).
-   [X] T003 Configure `uv` as the project's virtual environment manager.
-   [X] T004 Add initial empty files: `src/calculator/__init__.py`, `src/calculator/logic.py`, `src/calculator/ui.py`, `src/calculator/main.py`, `tests/__init__.py`, `tests/test_logic.py`.

## Phase 2: Core Logic Engine (TDD)

**Goal**: Implement the core calculation engine.
**Independent Test**: The `logic` module can be tested independently via `pytest`.

-   [X] T005 [US1] Write a failing test in `tests/test_logic.py` for basic addition.
-   [X] T006 [US1] Implement the simplest form of the `evaluate` function in `src/calculator/logic.py` to make the addition test pass.
-   [X] T007 [US1] Write failing tests for subtraction, multiplication, and division in `tests/test_logic.py`.
-   [X] T008 [US1] Extend the `evaluate` function to handle all basic arithmetic operations.
-   [X] T009 [US2] Write a failing test for order of operations using parentheses in `tests/test_logic.py`.
-   [X] T010 [US2] Enhance the expression parser in `src/calculator/logic.py` to correctly handle parentheses.
-   [X] T011 [US3] Write a failing test for division by zero in `tests/test_logic.py`.
-   [ ] T012 [US3] Add error handling in `src/calculator/logic.py` to raise `ZeroDivisionError`.
-   [X] T013 [US3] Write failing tests for other mathematical errors (e.g., invalid operator) in `tests/test_logic.py`.
-   [X] T014 [US3] Implement robust error handling for invalid expressions, raising a custom `InvalidExpressionError`.

## Phase 3: UI Development

**Goal**: Create the user interface for the calculator.
**Independent Test**: The UI can be launched and visually inspected, though logic will be disconnected.

-   [X] T015 [P] Design the main window and layout for the calculator in `src/calculator/ui.py`.
-   [X] T016 [P] Create the display widget for showing the expression and result in `src/calculator/ui.py`.
-   [X] T017 [P] Create all the calculator buttons (0-9, operators, special functions) in `src/calculator/ui.py`.
-   [X] T018 Connect button signals to placeholder slots in `src/calculator/ui.py` (e.g., a button click prints its value).

## Phase 4: Integration

**Goal**: Connect the UI to the core logic engine.

-   [X] T019 In `src/calculator/main.py`, connect the UI button signals to the `logic.evaluate` function.
-   [X] T020 Update the display with the current expression as buttons are pressed.
-   [X] T021 When the "=" button is pressed, call the `evaluate` function and display the result or error message.
-   [ ] T022 Implement the "Clear" (C) and "Clear Entry" (CE) functionality.

## Phase 5: Polish & Final Touches

**Goal**: Ensure a high-quality user experience.

-   [ ] T023 [P] Apply a stylesheet (QSS) to the PyQt application to achieve a "beautiful UI" in `src/calculator/ui.py`.
-   [ ] T024 [P] Add keyboard support for calculator input in `src/calculator/main.py`.
-   [ ] T025 Add an "About" dialog.
-   [ ] T026 Final review and refactoring of the entire codebase.
