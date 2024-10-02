from pathlib import Path
import json

def main():
    greet_user()

def greet_user():
    path = Path("username.json")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("File does not exist")
    else:
        
        username = json.loads(contents)
        print(f"Welcome {username}")
        
if __name__ == "__main__":
    main()
