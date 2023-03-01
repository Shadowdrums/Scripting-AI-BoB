# Scripting-AI-BoB
This is a basic AI designed to learn python scripting

This program is a Python bot that continuously creates and writes new Python scripts in a specific format, named "sandbox-N.py" where N is a number that increments with each new script. The bot looks for other Python scripts in the current directory and its subdirectories to learn from and use in its own script building. It also creates a new subdirectory named "AI-Scripting-Tests" to store the generated scripts.

The bot takes up to two minutes per script to generate, and it checks if the script is complete before writing it to the file. It also ensures that it does not read or learn from its own scripts to avoid copying or repeating its own code.

The program has a series of comments to help understand what each block of code does and any debugging or troubleshooting notes that may be relevant. Overall, this program is an example of a simple AI-powered script generator that can continue to learn and generate new scripts as long as it is running.
