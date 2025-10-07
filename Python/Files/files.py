
import os
from pathlib  import Path
# import hashlib

# script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = Path(__file__).resolve().parent

def create_file(filename, content=None):
    file_path = os.path.join(script_dir, filename)

    # If file exists → append
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            if content:
                file.write(content)
    else:
        # Create new file
        with open(file_path, "w") as file:
            if content:
                file.write(content)

def read_print_content(file_name):
    file_path = script_dir / file_name
    if file_path.exists():
        # with open(file_path, "r") as file:
        #     content = file.read()
        content = file_path.read_text(encoding="utf-8")
        print(content)
    else:
        print(f"{file_name} not found in {script_dir}")

def delete_file(file_name):
    file_path = script_dir / file_name
    if file_path.exists():
        os.remove(file_path)
        print(f"{file_name} deleted Successfully. ")
    else:
        print(f"{file_name} doesn't exist.")


if __name__ == "__main__":

    create_file("hi.txt", "Hi, How are You!\n")

    read_print_content("hi.txt")
    delete_file("hi.txt")