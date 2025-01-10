Feature:  Manage a To-Do list
    Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user lists all tasks
    Then the output should contains
    | Task           |
            | Buy groceries  |
            | Pay bills      |

    Scenario: Mark a task as completed
    Given the to-do list contains tasks
    | Task | Status |
    | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

    Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty

    Scenario: Display the information of a task
    Given the to-do list contains tasks
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user wants to display the information of the task "Pay bills"
    Then the to-do list displays the information of the task "Pay bills"

    Scenario: Modify the name of a task
    Given the to-do list contains tasks
    | Task |
    | Buy groceries |
    | Pay bills |
    When the user wants to change the name of the task "Buy groceries" to "Buy sweets"
    Then the to-do list reflects the change