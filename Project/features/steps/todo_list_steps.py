from behave import given, when, then
from todo_list import Task, ToDoList

# Scenario 1: Add a task to the to-do list
@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_then_todo_list_should_contain_task(context, task_name):
    task_names = [task.task_name for task in context.todo_list.tasks]
    assert task_name in task_names, f'Task "{task_name}" not found in the list.'


# Scenario 2: List all tasks
@given('the to-do list contains tasks')
def step_given_list_with_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

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
    context.todo_list.complete_task(task_name)

@then('the to-do list should show task "{task_name}" as completed')
def step_then_task_should_be_completed(context, task_name):
    for task in context.todo_list.tasks:
        if task.task_name == task_name:
            assert task.status == "Completed", f'Task "{task_name}" is not completed yet.'


# Scenario 4: Clear the entire to-do list
#Given the to-do list contains tasks:
@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    context.todo_list.clear_to_do_list()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.todo_list.tasks) == 0, "The to-do list is not empty."


# Scenario 5: Display the information of a task
#Given the to-do list contains tasks:
@when('the user wants to display the information of the task "{task_name}"')
def step_when_user_displays_task(context, task_name):
    context.output = []
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.todo_list.display_task(task_name)
    sys.stdout = sys.__stdout__ 
    context.output = captured_output.getvalue().splitlines()
    print(context.output)

@then('the to-do list displays the information of the task "{task_name}"')
def step_then_display_task_info(context, task_name):
    assert f'Task {task_name} not found.' not in context.output, 'Task {task_name} doesn\'t exists in the list'


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
