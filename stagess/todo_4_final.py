import json
import os

FILE = "tasks.json"


def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


tasks = load()  # each task: {"title": str, "done": bool}


def show():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark} {t['title']}")


def ask_number(prompt):
    num = input(prompt).strip()
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        return int(num) - 1
    print("Invalid number.")
    return None


def add():
    title = input("Task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save()


def delete():
    show()
    if not tasks:
        return
    idx = ask_number("Task number to delete: ")
    if idx is not None:
        removed = tasks.pop(idx)
        save()
        print(f"Deleted: {removed['title']}")


def done():
    show()
    if not tasks:
        return
    idx = ask_number("Task number to mark as done: ")
    if idx is not None:
        tasks[idx]["done"] = True
        save()
        print(f"Done: {tasks[idx]['title']}")


while True:
    cmd = input("add / show / done / delete / quit: ").strip().lower()
    if cmd == "add":
        add()
    elif cmd == "show":
        show()
    elif cmd == "done":
        done()
    elif cmd == "delete":
        delete()
    elif cmd == "quit":
        break
    else:
        print("Unknown command.")
