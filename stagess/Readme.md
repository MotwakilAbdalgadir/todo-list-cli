# Todo CLI

A simple command-line To-Do List application written in Python.

## Purpose

The purpose of this project is to help users organize their daily work by
managing a list of tasks directly from the terminal. It was built as a final
project to practice Python programming and the Git/GitHub workflow
(repositories, branches, commits, pull requests, and merging).

## Key Features

- **Add** a new task
- **Show** all tasks with their status (`[ ]` pending, `[x]` done)
- **Mark** a task as done
- **Delete** a task
- **Save automatically** to a `tasks.json` file, so tasks are kept after closing the program
- Input validation (empty tasks and invalid task numbers are rejected)

## Requirements

- Python 3.8 or newer (no external libraries needed)

## How to Run

```bash
git clone https://github.com/MotwakilAbdalgadir/todo-list-cli
cd todo-cli
python todo.py
```

## Usage

When the program starts, type one of the following commands:

| Command  | Description                     |
| -------- | ------------------------------- |
| `add`    | Add a new task                  |
| `show`   | Display all tasks               |
| `done`   | Mark a task as done (by number) |
| `delete` | Delete a task (by number)       |
| `quit`   | Exit the program                |

Example:

```
add / show / done / delete / quit: add
Task: Study for the exam
add / show / done / delete / quit: show
1. [ ] Study for the exam
add / show / done / delete / quit: done
Task number to mark as done: 1
```

## Git Workflow

Each significant change was developed in its own branch and merged into `main`
through a Pull Request:

- `feature-delete-task` – added the delete command
- `feature-mark-done` – added the done command and task status
- `feature-save-tasks` – added saving to `tasks.json` and empty-input fix
- `add-readme` – improved the documentation

## Contributors

- متوكل عبد القادر البشرى
- الرميصاء حسن الشامي
