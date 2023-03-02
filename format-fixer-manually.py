import os
import tokenize
import re
import sys
import ast

INDENT_SIZE = 4 # number of spaces per indent level

def replace_tabs_with_spaces(line, indent_size):
    """Replace tabs with spaces in a line of code"""
    leading_tabs = line.lstrip('\t')
    num_spaces = indent_size * (len(line) - len(leading_tabs) // len('\t'))
    return ' ' * num_spaces + leading_tabs

def reindent_file(filename):
    """Reindent a Python file to use spaces instead of tabs"""
    with open(filename, 'r') as f:
        source = f.read()

    # Parse the source with the ast module to get the syntax tree
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Failed to fix {filename} for PEP8 compliance: {e}")
        return

    # Determine the initial indent level of the file
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            initial_indent = node.col_offset
            break
    else:
        initial_indent = 0

    # Generate new source code with the ast module
    new_source = ast.unparse(tree)

    # Replace tabs with spaces in each line of the file
    new_lines = []
    for line in new_source.splitlines():
        if '\t' in line:
            new_line = replace_tabs_with_spaces(line, INDENT_SIZE)
            if len(line) - len(line.lstrip()) == initial_indent:
                new_line = ' ' * initial_indent + new_line.lstrip()
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Overwrite the file with the new lines
    with open(filename, 'w') as f:
        f.write('\n'.join(new_lines))

    print(f"Fixed {filename} for PEP8 compliance.")

def main():
    # Get list of Python files in current directory
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]

    # Print list of Python files
    print("Python files in current directory:")
    for i, filename in enumerate(py_files):
        print(f"{i+1}. {filename}")

    # Prompt user to choose a file
    while True:
        try:
            choice = int(input("Enter number of file to fix: "))
            filename = py_files[choice-1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number from the list.")

    # Reindent the selected Python file
    reindent_file(filename)

if __name__ == '__main__':
    main()
