import os
import random
import time
import glob
import sqlite3
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import openai
import re
# Replace with your OpenAI API key
openai.api_key = "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"


output_dir = os.getcwd()
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    sid = SentimentIntensityAnalyzer()
    sid.polarity_scores('test')
except LookupError:
    nltk.download('vader_lexicon')

db_conn = sqlite3.connect("BoB-Database")
db_cursor = db_conn.cursor()
db_cursor.execute('''CREATE TABLE IF NOT EXISTS scripts (id INTEGER PRIMARY KEY AUTOINCREMENT, script TEXT)''')
db_conn.commit()

def generate_script():
    scripts = [f for f in glob.glob(os.path.join(output_dir, '**/*.py'), recursive=True) 
               if not (f.endswith('.py') and 
                       (re.match(r'^test-\d+\.py$', os.path.basename(f)) or 
                        re.match(r'^Test-\d+\.py$', os.path.basename(f))))]
    script = ''
    for f in scripts:
        with open(f, 'r') as file:
            script += file.read()

    generated_script = ''
    while True:
        generated_script += random.choice(script.split('\n')) + '\n'
        script_size = len(generated_script.split('\n'))
        if script_size > 1:
            script_file_name = os.path.join(output_dir, f'Test-{time.time()}.py')
            with open(script_file_name, 'w') as f:
                f.write(generated_script)
            generated_script = generated_script.strip().replace('\n', '\n    ')
            print(f"Generated script: \n\n    {generated_script}")
            break

    return generated_script

def analyze_sentiment(script):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(script)

def learning_with_nlp():
    while True:
        goal = input("What is your goal for the script? ")
        print(f"Goal of the script: {goal}")

        generated_script = ''
        feedback = ''
        while not feedback:
            input("Press Enter to generate a new script")
            prompt = f"Generate a script that {goal}"
            completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
            generated_script = completions.choices[0].text
            generated_script = re.sub('[^0-9a-zA-Z\n\.\,\(\)\[\]\{\}\_\+\-\=\*\&\^\%\$\#\@\!\~\`\?\>\<\:\;\'\"\|\\\]', '', generated_script)
            generated_script = generated_script.strip()
            sentiment_scores = analyze_sentiment(generated_script)
            generated_script_formatted = generated_script.strip().replace('\n', '\n    ')
            print(f"Generated script: \n\n    {generated_script_formatted}")
            script_file_name = os.path.join(output_dir, f'Test-{time.time()}.py')
            with open(script_file_name, 'w') as f:
                f.write(generated_script)
            feedback = input("Did the generated script achieve the goal? (y/n): ")
            if feedback.lower() == 'n':
                generated_script = ''
                feedback = ''

        db_cursor.execute('''INSERT INTO scripts(script) VALUES (?)''', (generated_script,))
        db_conn.commit()

if __name__ == '__main__':
    learning_with_nlp()
