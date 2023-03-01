import os
import time
import random

# Set the maximum time limit for writing a script
MAX_TIME = 120

# Create a new subfolder for saving the output files
if not os.path.exists("AI-Scripting-Tests"):
    os.makedirs("AI-Scripting-Tests")

# Initialize a counter for the sandbox files
sandbox_num = 1

# Start an infinite loop to keep the program running
while True:

    # Generate a new sandbox file name
    sandbox_file = f"sandbox-{sandbox_num}.py"
    
    # Check if the file already exists (in case of a previous run)
    while os.path.exists(sandbox_file):
        sandbox_num += 1
        sandbox_file = f"sandbox-{sandbox_num}.py"
    
    # Open the sandbox file for writing
    with open(sandbox_file, "w") as f:
        
        # Get a list of all Python scripts in the current directory and its subfolders
        scripts = []
        for root, dirs, files in os.walk(".", topdown=True):
            dirs[:] = [d for d in dirs if d != "AI-Scripting-Tests"]  # Exclude the output subfolder
            for file in files:
                if file.endswith(".py") and file != sandbox_file:  # Exclude the current sandbox file
                    scripts.append(os.path.join(root, file))
        
        # Loop until the time limit is reached
        start_time = time.time()
        while time.time() - start_time < MAX_TIME:
            
            # Choose a random script to read and learn from
            script = random.choice(scripts)
            
            # Open the script file for reading
            with open(script, "r") as script_file:
                lines = script_file.readlines()
                
                # Loop through each line of the script and add it to the sandbox file
                for line in lines:
                    f.write(line)
                    
                    # Check if the time limit has been reached, and if so, save the sandbox file and start over
                    if time.time() - start_time >= MAX_TIME:
                        f.close()
                        sandbox_num += 1
                        break
            
            # Check if the time limit has been reached, and if so, save the sandbox file and start over
            if time.time() - start_time >= MAX_TIME:
                break
    
    # Increment the sandbox counter for the next iteration
    sandbox_num += 1
