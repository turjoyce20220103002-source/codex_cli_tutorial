# Codex CLI Tool Tutorial

Welcome to the Codex CLI tool tutorial! This guide will walk you through the installation and usage of Codex.

## 1. Installation

To use Codex, you first need to install it. Open your terminal or command prompt, navigate to the `codex_cli_tutorial` directory, and run the following command:

```bash
pip install .
```

This command will install the `codex` tool and make it available in your terminal.

## 2. Usage

Codex provides several commands to help you with your development tasks.

### 2.1. Creating Files

To create a new file, use the `codex create file` command, followed by the name of the file you want to create.

**Example:**

```bash
codex create file my_new_file.txt
```

This will create an empty file named `my_new_file.txt` in your current directory.

### 2.2. Creating Directories

To create a new directory, use the `codex create dir` command, followed by the name of the directory.

**Example:**

```bash
codex create dir my_new_folder
```

This will create a new directory named `my_new_folder` in your current directory.

### 2.3. Counting Lines of Code

Codex can count the total number of lines in a file or in all files within a directory.

#### Counting Lines in a Single File

To count the lines in a single file, use the `codex count lines` command, followed by the path to the file.

**Example:**

```bash
codex count lines my_app/main.py
```

#### Counting Lines in a Directory

To count the lines in all files within a directory (and its subdirectories), provide the path to the directory.

**Example:**

```bash
codex count lines my_app
```

This will recursively count the lines of all files in the `my_app` directory.

## 3. Getting Help

You can always get help and see the available commands by running `codex` with the `--help` or `-h` flag.

```bash
codex --help
```

To get help for a specific subcommand, use the `--help` flag after the subcommand.

**Example:**

```bash
codex create --help
codex count lines --help
```

---

That's it! You now know how to use the basic features of the Codex CLI tool.
