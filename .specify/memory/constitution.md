<!--
---
version_change: "1.1.0 -> 1.2.0"
modified_principles:
  - Code Style
added_sections:
  - Core Principles: VII. Embrace Object-Oriented Design
  - Code Style: Clean Code Practices
removed_sections: []
templates_updated: []
follow_up_todos: []
---
-->
# Simple Calculator Constitution

## 1. Core Principles

### I. Enforce Strict Type Safety
All new code must include PEP 484-compliant type hints. This will be enforced by `mypy` in strict mode.

### II. Maintain Minimalist Dependencies
Only `pytest` and essential development tools (`ruff`, `mypy`) are permitted as development-only dependencies. No additional runtime dependencies are allowed for the MVP.

### III. Adhere to Standardized Tooling
The project exclusively uses `uv`, `pytest`, `ruff`, and `mypy` for environment management, testing, code formatting, and type checking.

### IV. Use Standard Library for UI
The Minimum Viable Product (MVP) will use Tkinter for its graphical user interface. No external GUI libraries are to be introduced.

### V. Practice Test-Driven Development (TDD)
All new features or bug fixes must be accompanied by comprehensive unit and integration tests written with `pytest`.

### VI. Centralize Configuration
All project configuration must be managed within `pyproject.toml`. No `requirements.txt` or `Pipfile` files are to be used.

### VII. Embrace Object-Oriented Design
The calculator's core logic, including its state and operations, must be encapsulated within classes. The design should favor composition over inheritance and follow SOLID principles where applicable.

## 2. Code Style & Clean Code Practices
- **Formatting**: Code will be auto-formatted using `ruff format`.
- **Linting**: Code quality will be enforced using `ruff check`.
- **Imports**: Imports must be automatically sorted by `ruff`.
- **Descriptive Naming**: All variables, functions, methods, and classes must have clear, descriptive names that reveal their intent.
- **Single Responsibility**: Functions and classes should be small and adhere to the Single Responsibility Principle.
- **Documentation**: All public modules, classes, and functions must have docstrings explaining their purpose, arguments, and return values.

## 3. Testing
- **Framework**: `pytest` is the sole framework for all tests.
- **Coverage**: Every new feature must be accompanied by tests.
- **TDD**: Follow the Red-Green-Refactor cycle. Write a failing test before writing implementation code.

## 4. Development Workflow
- **Branching**:
  - `main`: Production-ready, stable code.
  - `develop`: Integration branch for features.
  - `feature/<name>`: For new features or bug fixes.
- **Commits**: Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
- **Pull Requests (PRs)**:
  - All work must be submitted via PRs to the `develop` branch.
  - PRs must pass all automated checks (linting, type checking, testing).
  - PRs require at least one approving review.

## 5. Versioning
This project adheres to [Semantic Versioning 2.0.0](https://semver.org/). Version numbers (MAJOR.MINOR.PATCH) will be updated as follows:
- **MAJOR**: For incompatible API changes.
- **MINOR**: For new, backward-compatible functionality.
- **PATCH**: For backward-compatible bug fixes.

## 6. Project Technology Stack
| Category              | Tool / Standard                  |
| --------------------- | -------------------------------- |
| **Language**          | Python 3.12+                     |
| **Package Manager**   | `uv`                             |
| **Project Config**    | `pyproject.toml`                 |
| **UI Framework**      | Tkinter                          |
| **Testing**           | `pytest`                         |
| **Linting/Formatting**| `ruff`                           |
| **Type Checking**     | `mypy` (strict)                  |

## 7. Governance
All contributions must align with this constitution. Any proposed deviation requires a documented ADR (Architectural Decision Record) and formal approval.

**Version**: 1.2.0 | **Ratified**: 2025-12-19 | **Last Amended**: 2025-12-19