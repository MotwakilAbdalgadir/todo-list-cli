tasks = []


def show():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


while True:
    cmd = input("add / show / quit: ").strip().lower()
    if cmd == "add":
        tasks.append(input("Task: ").strip())
    elif cmd == "show":
        show()
    elif cmd == "quit":
        break
    else:
        print("Unknown command.")
