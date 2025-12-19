# Data Model

This feature is primarily focused on a user interface and real-time calculation logic. As such, it does not have a complex data persistence model. The key data entities are transient and exist within the application's state.

## Core Entities

### Calculation

-   **Description**: Represents a single calculation performed by the user.
-   **Attributes**:
    -   `expression` (str): The mathematical expression input by the user (e.g., "2+2").
    -   `result` (float | str): The computed result of the expression, or an error message.
    -   `timestamp` (datetime): The time when the calculation was performed.
-   **State**: This entity is used to manage the application's history.

### Application State

-   **Description**: Represents the current state of the calculator UI.
-   **Attributes**:
    -   `current_expression` (str): The expression currently being built in the display.
    -   `memory` (float): The value stored in the calculator's memory.
    -   `history` (List[Calculation]): A list of past calculations.
