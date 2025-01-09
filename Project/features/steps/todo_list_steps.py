from behave import given, when, then
from todo_list import Task, ToDoList  # Ensure these classes are imported correctly

# Scenario 1: Add a task to the to-do list
@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()  # Initialize an empty to-do list

@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    context.todo_list.add_task(task_name)  # Add the task with the given name

@then('the to-do list should contain "{task_name}"')
def step_then_todo_list_should_contain_task(context, task_name):
    task_names = [task.task_name for task in context.todo_list.tasks]  # Get task names
    assert task_name in task_names, f'Task "{task_name}" not found in the list.'  # Check if task is in the list


# Scenario 2: List all tasks
@given('the to-do list contains tasks')
def step_given_list_with_tasks(context):
    context.todo_list = ToDoList()  # Initialize the to-do list
    for row in context.table:
        context.todo_list.add_task(row['Task'])  # Add tasks from the table

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.output = []
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.todo_list.list_tasks()
    sys.stdout = sys.__stdout__ 
    context.output = captured_output.getvalue().splitlines()

@then('the output should contains')
def step_then_output_should_contain(context):
    for row in context.table:
        task_name = row['Task']
        expected_output = f"- {task_name}"
        assert any(expected_output in line for line in context.output), f"Expected '{task_name}' to be in output."


# Scenario 3: Mark a task as completed
#Given the to-do list contains tasks:
@when('the user marks task "{task_name}" as completed')
def step_when_user_marks_task_as_completed(context, task_name):
    context.todo_list.complete_task(task_name)  # Mark the task as completed

@then('the to-do list should show task "{task_name}" as completed')
def step_then_task_should_be_completed(context, task_name):
    for task in context.todo_list.tasks:
        if task.task_name == task_name:
            assert task.status == "Completed", f'Task "{task_name}" is not completed yet.'  # Check the task's status


# Scenario 4: Clear the entire to-do list
#Given the to-do list contains tasks:
@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    context.todo_list.clear_to_do_list()  # Clear the to-do list

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.todo_list.tasks) == 0, "The to-do list is not empty."  # Check if the list is empty


# Scenario 5: Display the information of a task
#Given the to-do list contains tasks:
@when('the user wants to display the information of the task "{task_name}"')
def step_when_user_displays_task(context, task_name):
    context.output = []
    context.todo_list.display_task(task_name)  # Display the task's information

@then('the to-do list displays the information of that task')
def step_then_display_task_info(context):
    # Check if the output contains the expected information
    assert 'Task:' in context.output, 'Task info not displayed correctly.'
    assert 'Status:' in context.output, 'Task status not displayed correctly.'


# Scenario 6: Modify the name of a task
#Given the to-do list contains tasks:
@when('the user wants to change the name of the task "{old_name}" to "{new_name}"')
def step_when_user_modifies_task(context, old_name, new_name):
    context.todo_list.modify_task(old_name, new_name)  # Modify the task's name

@then('the to-do list reflects the change')
def step_then_todo_list_reflects_change(context):
    task_names = [task.task_name for task in context.todo_list.tasks]
    assert "Buy sweets" in task_names, "Task name was not changed correctly."
    assert "Buy groceries" not in task_names, "Old task name still present."
