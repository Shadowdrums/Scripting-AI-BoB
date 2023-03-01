# Scripting-AI-BoB
This is a basic AI designed to learn python scripting

This is a Python program that generates scripts using existing Python code and user-specified goals. It saves generated scripts to a directory called "AI-Scripting-Tests" in the current working directory, and asks the user for feedback on whether or not the generated script achieves the specified goal. If the user indicates that the script does not achieve the goal, the program generates another script with the same goal. If the user indicates that the script does achieve the goal, the program saves the script to the output directory and prompts the user for feedback on how the script can be improved.

The program also uses a SQLite database to store generated scripts. The database is created if it doesn't exist, and a table named "scripts" is created to store the generated scripts. The table has two columns: "id" (an auto-incrementing primary key) and "script" (a text column that stores the generated script). After a script is generated and the user indicates that it achieves the goal, the generated script is added to the "scripts" table in the database.

The program limits the size of the generated scripts to a maximum of 1000 lines. It also limits the time taken to generate a script to 60 seconds.

Overall, this program is an AI script generator that generates Python scripts based on existing code and user-specified goals, saves the generated scripts to a directory and a database, and prompts the user for feedback to improve the scripts.
