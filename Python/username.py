from pathlib import Path
import json

def main():
    print(get_username())

def get_username():
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        username = input("what is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        return username

def add_new_user(new):
    path = Path("username.json")
    contents = json.dumps(new)
    path.write_text(contents)
    
    
    
if __name__ == "__main__":
    main()
