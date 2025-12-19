# Research & Decisions

## UI Framework Selection

-   **Decision**: Use `PyQt`.
-   **Rationale**: `PyQt` is a mature, well-documented, and powerful framework for creating professional-looking desktop applications that can be styled to be "beautiful," as per the user's request. It offers a wider range of modern widgets and better styling capabilities compared to Tkinter. Its cross-platform nature ensures the calculator can run on Windows, macOS, and Linux.
-   **Alternatives considered**:
    -   **Kivy**: While also cross-platform, Kivy is primarily targeted at multi-touch applications (mobile, tablets) and has a distinct look and feel that may be less conventional for a desktop calculator.
    -   **Tkinter**: The standard library option. It's simple and good for basic UIs, but it does not meet the "beautiful" and "world-class" criteria specified by the user.
