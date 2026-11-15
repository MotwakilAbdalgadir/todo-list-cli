tasks = []


def show():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


def delete():
    show()
    if not tasks:
        return
    num = input("Task number to delete: ").strip()
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        removed = tasks.pop(int(num) - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid number.")


while True:
    cmd = input("add / show / delete / quit: ").strip().lower()
    if cmd == "add":
        tasks.append(input("Task: ").strip())
    elif cmd == "show":
        show()
    elif cmd == "delete":
        delete()
    elif cmd == "quit":
        break
    else:
        print("Unknown command.")
