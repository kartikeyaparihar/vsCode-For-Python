#write the python program to print the contents of directory using the os module search online for the function which does 
# that and here i am using chatgpt for that

import os

def print_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        print(f"Contents of directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

directory_path = 'D:\didi'  # Replace with your directory path
print_directory_contents(directory_path)
