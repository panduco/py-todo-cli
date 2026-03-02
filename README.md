# 📝 Python Todo CLI

A simple, lightweight, and fast command-line tool to manage your daily tasks. 
Built with Python as a demonstration of CLI design, file I/O handling, and package distribution.

## ✨ Features

- **Add Tasks:** Quickly add tasks to your list.
- **List Tasks:** View all pending and completed tasks in a clean format.
- **Complete Tasks:** Mark tasks as done when you finish them.
- **Delete Tasks:** Remove tasks you no longer need.
- **Clear All:** Wipe your entire task list with a safety confirmation.
- **Persistent Storage:** Tasks are saved in a local `tasks.json` file, so they remain even after closing the terminal.
- **Global Installation:** Can be installed and run from anywhere on your system.

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher.

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/py-todo-cli.git
   cd py-todo-cli
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install the package:**
   ```bash
   pip install -e .
   ```
   *(This installs the package in "editable" mode, allowing you to run the `todo` command globally in your terminal.)*

## 💻 Usage

Once installed, you can use the `todo` command from anywhere in your terminal.

### Add a new task
```bash
todo add "Buy groceries for the week"
```
**Output:**
```text
✅ Added: Buy groceries for the week
```

### List all tasks
```bash
todo list
```
**Output:**
```text
--- YOUR TASKS ---
1. [ ] Buy groceries for the week
2. [ ] Walk the dog
------------------
```

### Mark a task as done
Use the task number (ID) from the list.
```bash
todo done 1
```
**Output:**
```text
🎉 Task 1 marked as done!
```

### Delete a task
Remove a task entirely using its ID.
```bash
todo delete 1
```
**Output:**
```text
🗑️ Deleted: Buy groceries for the week
```

### Clear all tasks
Delete your entire task list. The program will ask for confirmation to prevent accidents.
```bash
todo clear
```
**Output:**
```text
Are you sure you want to delete all tasks? (y/n): y
🗑️ All tasks deleted.
```

### Help
View all available commands:
```bash
todo --help
```

## 📂 Project Structure

```
py-todo-cli/
├── todo.py        # Main application logic
├── setup.py       # Installation configuration
├── tasks.json     # Local database (auto-generated)
└── README.md      # Project documentation
```

## 🔧 Technologies Used

- **Python 3:** Core logic.
- **Argparse:** For parsing command-line arguments.
- **JSON:** For data persistence.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
