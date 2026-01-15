import argparse
import os
from rich import print
from rich.panel import Panel

def create_file(args):
    """Creates a new file."""
    try:
        with open(args.filename, 'w') as f:
            pass
        print(f"[bold green]File created:[/] {args.filename}")
    except IOError as e:
        print(f"[bold red]Error creating file:[/] {e}")

def create_dir(args):
    """Creates a new directory."""
    try:
        os.makedirs(args.dirname)
        print(f"[bold green]Directory created:[/] {args.dirname}")
    except OSError as e:
        print(f"[bold red]Error creating directory:[/] {e}")

def count_lines(args):
    """Counts the lines of code in a file or directory."""
    total_lines = 0
    if os.path.isfile(args.path):
        total_lines = _count_lines_in_file(args.path)
    elif os.path.isdir(args.path):
        for dirpath, _, filenames in os.walk(args.path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_lines += _count_lines_in_file(filepath)
    else:
        print(f"[bold red]Error: Path not found -[/] {args.path}")
        return

    print(Panel(f"[bold yellow]Total lines:[/] {total_lines}", title="Line Count"))

def _count_lines_in_file(filepath):
    """Helper function to count lines in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return len(f.readlines())
    except Exception:
        # Ignore files that can't be opened or read (e.g., binary files)
        return 0

def main():
    """Main function for the codex CLI tool."""
    parser = argparse.ArgumentParser(description="A simple CLI tool for developers.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a file or directory")
    create_subparsers = create_parser.add_subparsers(dest="create_command")

    # Create file command
    create_file_parser = create_subparsers.add_parser("file", help="Create a file")
    create_file_parser.add_argument("filename", help="The name of the file to create")
    create_file_parser.set_defaults(func=create_file)

    # Create directory command
    create_dir_parser = create_subparsers.add_parser("dir", help="Create a directory")
    create_dir_parser.add_argument("dirname", help="The name of the directory to create")
    create_dir_parser.set_defaults(func=create_dir)

    # Count command
    count_parser = subparsers.add_parser("count", help="Count lines of code")
    count_subparsers = count_parser.add_subparsers(dest="count_command")

    # Count lines command
    count_lines_parser = count_subparsers.add_parser("lines", help="Count lines in a file or directory")
    count_lines_parser.add_argument("path", help="The path to the file or directory")
    count_lines_parser.set_defaults(func=count_lines)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()