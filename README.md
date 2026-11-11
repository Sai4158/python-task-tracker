# Python Task Tracker

A command-line Python learning project built step by step with generative AI.

## Features

- Add tasks with nonblank descriptions.
- View numbered tasks with Pending or Completed status.
- Mark a task as completed.
- Delete a task by its displayed number.
- Repeat the menu until option 5 (Exit) is selected.
- Handle invalid menu choices, nonnumeric task numbers, zero, negative numbers,
  numbers outside the list, and empty task lists without crashing.

Tasks are stored in a list of dictionaries. Each dictionary contains a
`description` string and a `completed` Boolean (`True` or `False`). Tasks are
stored in memory only and cleared when the program exits. Task numbers reflect
the current list order and are updated after deletion.

The program uses Python 3 and requires no external packages, database, login,
graphical interface, or file saving.

## Run

Open PowerShell in the project folder and run:

```powershell
cd "C:\Users\saira\Documents\Python Task Tracker\python-task-tracker"
py task_tracker.py
```

If the Python launcher (`py`) is unavailable, use `python task_tracker.py`.
Choose a menu option from 1 to 5 and follow the prompts. Options 3 and 4 show
the task list before asking for a task number. Invalid input returns to the menu.

## Code guide

- `main()` creates the task list and runs the repeating menu.
- `show_menu()` prints the five available actions.
- `add_task()` trims the description, rejects blank input, and adds a pending task.
- `view_tasks()` displays task numbers and status, or an empty-list message.
- `get_task_index()` checks task-number input and converts it to a list index.
- `complete_task()` updates a task's completed status.
- `delete_task()` removes a task from the list.

## Manual checks

- View, complete, and delete tasks when the list is empty.
- Add two tasks and confirm that both show as Pending.
- Try a blank or spaces-only description and confirm it is rejected.
- Complete one task and confirm its status changes to Completed.
- Try invalid menu choices and task numbers such as `hello`, `0`, `-1`, and `99`.
- Delete a task and confirm the remaining tasks are renumbered.
- Exit with option 5, then restart and confirm the list is empty.

## Progress

- Project initialized with a runnable starter.
- Repeating menu and all core task operations implemented.
