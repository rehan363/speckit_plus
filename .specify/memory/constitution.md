<!--
---
version_change: "1.2.0 -> 1.3.0"
modified_principles:
  - "Core Principles"
  - "Code Style & Clean Code Practices"
  - "Development Workflow"
  - "Project Technology Stack"
added_sections:
  - "Accessibility (a11y)"
  - "Internationalization (i18n)"
  - "Extensibility and Plugins"
removed_sections: []
templates_updated: []
follow_up_todos: []
---
-->
# World-Class Calculator Constitution

## 1. Core Principles

### I. Enforce Strict Type Safety
All new code must include PEP 484-compliant type hints, enforced by `mypy` in strict mode. This ensures code is robust, readable, and maintainable.

### II. Embrace a Rich, Modern UI/UX
The project will evolve beyond a minimal UI. While the initial MVP uses Tkinter, the long-term vision is to adopt a powerful, cross-platform framework like **PyQt** or **Kivy** to deliver a professional-grade user experience.

### III. Support Advanced Mathematical Capabilities
The calculator will not be limited to basic arithmetic. It will include:
- **Scientific Mode**: With trigonometric, logarithmic, and exponential functions.
- **Graphing Mode**: For visualizing equations and data.
- **Statistical and Financial Functions**: To cater to a wider range of users.
This implies the controlled and justified inclusion of libraries like `NumPy`, `SciPy`, and `Matplotlib`.

### IV. Design for Extensibility
The calculator should be designed with a **plugin architecture**. This will allow the community to add new functions, themes, and integrations without modifying the core codebase.

### V. Champion Accessibility (a11y)
A world-class application is usable by everyone. The UI must adhere to accessibility best practices, including keyboard navigation, screen reader support, and sufficient color contrast.

### VI. Prioritize Performance
For complex calculations and real-time graphing, performance is key. The development process must include:
- **Performance Profiling**: To identify and eliminate bottlenecks.
- **Efficient Algorithms**: Choosing data structures and algorithms that scale.

### VII. Plan for Internationalization (i18n) and Localization (l10n)
The application must be designed to support multiple languages and regional formats. This includes separating user-facing strings into resource files from the start.

### VIII. Allow User Customization
Users should have control over the calculator's appearance and behavior. This includes a settings panel for managing themes, precision, and other preferences.

### IX. Practice Test-Driven Development (TDD)
All new features or bug fixes must be accompanied by comprehensive unit, integration, and UI tests written with `pytest`. The Red-Green-Refactor cycle is mandatory.

### X. Centralize Configuration
All project configuration must be managed within `pyproject.toml`.

## 2. Code Style & Clean Code Practices
- **Formatting & Linting**: Code will be auto-formatted and checked using `ruff`.
- **Descriptive Naming**: All variables, functions, and classes must have clear names that reveal their intent.
- **SOLID Principles**: The codebase will adhere to SOLID principles, with a focus on the Single Responsibility Principle and encapsulation.
- **Comprehensive Documentation**: All public modules, classes, and functions must have clear docstrings.

## 3. Testing
- **Framework**: `pytest` is the sole framework for all tests.
- **Coverage**: Every new feature must be accompanied by tests to ensure high code coverage.
- **TDD**: Follow the Red-Green-Refactor cycle.

## 4. Development Workflow
- **Branching**: `main` (stable), `develop` (integration), `feature/<name>` (work).
- **Commits**: Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
- **CI/CD**: A full Continuous Integration/Continuous Deployment pipeline will be set up using **GitHub Actions**. All PRs must pass automated checks (linting, testing, type checking) before being merged into `develop`.
- **Pull Requests (PRs)**: Require at least one approving review.

## 5. Versioning
This project adheres to [Semantic Versioning 2.0.0](https://semver.org/).

## 6. Project Technology Stack
| Category                  | Tool / Standard                      |
| ------------------------- | ------------------------------------ |
| **Language**              | Python 3.12+                         |
| **Package Manager**       | `uv`                                 |
| **Project Config**        | `pyproject.toml`                     |
| **UI Framework (MVP)**    | Tkinter                              |
| **UI Framework (Pro)**    | PyQt / Kivy (to be decided via ADR)  |
| **Scientific Computing**  | `NumPy`, `SciPy`                     |
| **Plotting/Graphing**     | `Matplotlib`                         |
| **Testing**               | `pytest`                             |
| **Linting/Formatting**    | `ruff`                               |
| **Type Checking**         | `mypy` (strict)                      |
| **CI/CD**                 | GitHub Actions                       |

## 7. Governance
All contributions must align with this constitution. Any proposed deviation requires a documented ADR (Architectural Decision Record) and formal approval.

**Version**: 1.3.0 | **Ratified**: 2025-12-19 | **Last Amended**: 2025-12-19