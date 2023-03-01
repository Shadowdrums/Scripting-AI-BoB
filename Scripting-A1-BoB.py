import os
import random
import time
import glob
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(dir_path, 'AI-Scripting-Tests')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

db_conn = sqlite3.connect("BoB-Database")
db_cursor = db_conn.cursor()
db_cursor.execute('''CREATE TABLE IF NOT EXISTS scripts
                (id INTEGER PRIMARY KEY AUTOINCREMENT, script TEXT)''')
db_conn.commit()

MAX_SCRIPT_SIZE = 1000

def generate_script():
    scripts = [f for f in glob.glob(os.path.join(dir_path, '**/*.py'), recursive=True) if not f.endswith('sandbox.py')]
    script = ''
    for f in scripts:
        with open(f, 'r') as file:
            script += file.read()

    generated_script = ''
    start_time = time.time()
    while len(generated_script.split('\n')) < MAX_SCRIPT_SIZE and time.time() - start_time < 60:
        generated_script += random.choice(script.split('\n')) + '\n'

    return generated_script

while True:
    goal = input("Enter the goal of the script: ")
    input(f"Press Enter to generate a new script with the goal: {goal}")
    generated_script = generate_script()
    print(f"Generated script:\n{generated_script}")

    filename = f"sandbox-{time.time()}.py"
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w") as file:
        file.write(generated_script)

    feedback = input("Did the script achieve the goal? (y/n)")
    if feedback.lower() == "n":
        continue

    db_cursor.execute("INSERT INTO scripts (script) VALUES (?)", (generated_script,))
    db_conn.commit()

    more_feedback = input("How can the script be improved?")
    with open(output_path, "a") as file:
        file.write(f"\n\nFeedback:\n{more_feedback}\n")

    print(f"Script saved to {output_path}\n")
