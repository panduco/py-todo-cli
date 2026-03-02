import argparse
import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, 'r') as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="A simple CLI Todo List")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ADD Command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task", type=str, help="The task description")

    # LIST Command
    subparsers.add_parser("list", help="List all tasks")

    # DONE Command
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("id", type=int, help="The task number to complete")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        tasks.append({"task": args.task, "done": False})
        save_tasks(tasks)
        print(f"✅ Added: {args.task}")

    elif args.command == "list":
        if not tasks:
            print("No tasks found! Add one using 'todo add \"task name\"'")
            return

        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, start=1):
            # This checks the 'done' status and displays [x] or [ ]
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['task']}")
        print("------------------\n")

    elif args.command == "done":
        try:
            task_idx = args.id - 1
            if 0 <= task_idx < len(tasks):
                tasks[task_idx]["done"] = True
                save_tasks(tasks)
                print(f"🎉 Task {args.id} marked as done!")
            else:
                print("Error: Task ID out of range.")
        except ValueError:
            print("Error: ID must be a number.")

if __name__ == "__main__":
    main()