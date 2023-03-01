# Scripting-AI-BoB
This is a basic AI designed to learn python scripting

The learning_with_nlp() function is the main function that utilizes OpenAI's API to generate Python scripts based on a given goal. The function starts by prompting the user to provide a goal for the script they want to generate.

Then, the function enters a loop that generates Python scripts and prompts the user for feedback on each script. The loop will continue until the user confirms that a generated script has achieved the goal.

In each iteration of the loop, the function uses OpenAI's Completion API to generate a Python script that achieves the provided goal. The API is called twice, once with the davinci engine and once with the text-davinci-002 engine. The davinci engine is a more powerful language model than text-davinci-002, but it also has higher costs. Therefore, using both engines can help balance the cost and performance of the script generation process.

After generating a Python script, the function uses the SentimentIntensityAnalyzer from the Natural Language Toolkit (NLTK) library to analyze the sentiment of the script. The sentiment analysis can help identify any potential issues with the generated script that may need to be addressed.

The generated script is then printed to the console, and the user is prompted to confirm whether or not the script has achieved the goal. If the user confirms that the goal has been achieved, the generated script is stored in a SQLite database. If not, the loop continues and generates a new script.

Finally, the function cleans up the generated script by removing any characters that are not alphanumeric or commonly used in Python code. The cleaned script is then written to a file with a unique name based on the current timestamp.
