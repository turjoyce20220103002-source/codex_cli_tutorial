# 🚀 Getting Started with Codex: A Step-by-Step Guide

Welcome to the official tutorial for the Codex CLI tool! This guide will walk you through everything you need to know to get up and running with Codex, from installation to advanced usage.

---

## 1. 💾 Installation

Before you can use Codex, you need to install it on your system. The installation is straightforward using `pip`.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/turjoyce20220103002-source/codex_cli_tutorial.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd codex_cli_tutorial
    ```
3.  **Install the tool:**
    ```bash
    pip install .
    ```

> **💡 Pro Tip:** The `pip install .` command installs the project in "editable" mode, which means any changes you make to the source code will be immediately available when you run the `codex` command.

---

## 2. 🛠️ Core Commands

Codex provides a set of commands to help you manage your projects. Here's a look at the core functionalities:

### 2.1. Creating Files

Need to create a new file quickly? Use the `codex create file` command.

**Usage:**
```bash
codex create file <filename>
```

**Example:**
```bash
codex create file README.md
```
This will create an empty file named `README.md` in your current directory. You'll see a confirmation message in your terminal:
```
File created: README.md
```

### 2.2. Creating Directories

To create a new directory (or folder), use the `codex create dir` command.

**Usage:**
```bash
codex create dir <dirname>
```

**Example:**
```bash
codex create dir src
```
This will create a new directory named `src`. The output will be:
```
Directory created: src
```

### 2.3. Counting Lines of Code

Get a quick sense of your project's scale with the `codex count lines` command. It works on both single files and entire directories.

**Usage (for a file):**
```bash
codex count lines <file_path>
```

**Usage (for a directory):**
```bash
codex count lines <directory_path>
```

**Example (file):**
```bash
codex count lines src/main.py
```

**Example (directory):**
```bash
codex count lines src
```
The tool will recursively scan the `src` directory and output the total number of lines in a formatted panel.

---

## 3. 🆘 Getting Help

If you ever forget a command or an option, Codex has a built-in help system.

**For a general overview of all commands:**
```bash
codex --help
```

**For help with a specific subcommand:**
```bash
codex <command> --help
```

**Example:**
```bash
codex create --help
codex count --help
```

---

## 🎉 Conclusion

You've now mastered the basics of the Codex CLI tool! You can create files and directories, count lines of code, and get help when you need it.

We encourage you to explore the tool and see how it can fit into your development workflow. Happy coding!