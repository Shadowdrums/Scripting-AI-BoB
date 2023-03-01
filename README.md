# Scripting-AI-BoB
This is a basic AI designed to learn python scripting

This is a Python script that uses OpenAI's API and Natural Language Processing (NLP) techniques to generate Python scripts based on a user-specified goal. The generated script is then evaluated by the user to determine if it has achieved the intended goal.

The script first imports the required libraries and sets up the OpenAI API key. It also creates a database (if it doesn't already exist) to store the generated scripts.

The generate_script() function takes a goal (specified by the user) and uses it as a prompt to generate a Python script using OpenAI's text generation model. The generated script is then cleaned up to remove any unwanted characters and stored in a file. The function returns the generated script.

The analyze_sentiment() function takes a script and uses the SentimentIntensityAnalyzer from the Natural Language Toolkit (NLTK) to determine the sentiment (positive, negative or neutral) of the script.

The learning_with_nlp() function is the main function that drives the script. It prompts the user to enter a goal for the script and then generates a Python script based on that goal. The user is then asked to evaluate the script and provide feedback. If the generated script did not achieve the goal, a new script is generated based on the same goal. The process continues until the user is satisfied with the generated script.

Overall, this script demonstrates how NLP and machine learning can be used to automate the process of generating code, making it easier and more efficient for developers to write programs.
