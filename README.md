# Scripting-AI-BoB
This is a basic AI designed to learn python scripting

This is a Python script that uses OpenAI's API and Natural Language Processing (NLP) techniques to generate Python scripts based on a user-specified goal. The generated script is then evaluated by the user to determine if it has achieved the intended goal.

The script first imports the required libraries and sets up the OpenAI API key. It also creates a database (if it doesn't already exist) to store the generated scripts.

The generate_script() function takes a goal (specified by the user) and uses it as a prompt to generate a Python script using OpenAI's text generation model. The generated script is then cleaned up to remove any unwanted characters and stored in a file. The function returns the generated script.

The analyze_sentiment() function takes a script and uses the SentimentIntensityAnalyzer from the Natural Language Toolkit (NLTK) to determine the sentiment (positive, negative or neutral) of the script.

The learning_with_nlp() function is the main function that drives the script. It prompts the user to enter a goal for the script and then generates a Python script based on that goal. The user is then asked to evaluate the script and provide feedback. If the generated script did not achieve the goal, a new script is generated based on the same goal. The process continues until the user is satisfied with the generated script.

Overall, this script demonstrates how NLP and machine learning can be used to automate the process of generating code, making it easier and more efficient for developers to write programs.

#### format-fixer-manually

This program is a Python script that takes a Python file as input and reindents it to use spaces instead of tabs, in accordance with the PEP8 style guide.

The program begins by importing several modules: os, tokenize, re, sys, and ast. The os module provides a way to interact with the file system, tokenize is used to tokenize the input source code, re is used for regular expressions, sys is used to interact with the Python interpreter, and ast is used to parse the input source code into an abstract syntax tree.

The program defines a constant called INDENT_SIZE, which is the number of spaces to use for each indent level. It also defines a function called replace_tabs_with_spaces, which takes a line of code and the indent size as input, and replaces any tabs in the line with the appropriate number of spaces. The function then returns the modified line.

The main function of the program is called main. It begins by getting a list of all the Python files in the current directory that end with the .py extension. It then prints out a list of these files, prompting the user to choose which file they want to reindent.

Once the user has selected a file, the program calls the reindent_file function, passing in the filename as input. The reindent_file function first reads the entire contents of the file into a string variable called source.

Next, the program uses the ast module to parse the source code into an abstract syntax tree called tree. If the parsing fails due to a syntax error, the function prints an error message and returns without making any changes to the file.

The function then walks the tree using the ast.walk function to find the initial indent level of the file. If there is a function definition in the file, the function uses the column offset of the function definition as the initial indent level. If there are no function definitions in the file, the initial indent level is set to zero.

Next, the function uses the ast.unparse function to generate a new source code string based on the modified abstract syntax tree. The new source code string is then split into lines, and each line is checked for tabs using the 'in' operator.

If a line contains tabs, the replace_tabs_with_spaces function is called to replace the tabs with the appropriate number of spaces. If the line is the first line of a block and has the same number of spaces as the initial indent level, the function also adds the initial indent level to the beginning of the line.

The modified lines are then added to a list called new_lines, which is used to build the new source code string. If a line does not contain tabs, it is simply added to the new_lines list without modification.

Finally, the function overwrites the original file with the new source code using the 'w' mode of the open function. The new_lines list is converted to a string with the join method, and the resulting string is written to the file. The function then prints a message to the console indicating that the file has been fixed for PEP8 compliance.

The main function simply gets a list of Python files in the current directory, prints the list to the console, prompts the user to choose a file, and then calls the reindent_file function to reindent the selected file.
