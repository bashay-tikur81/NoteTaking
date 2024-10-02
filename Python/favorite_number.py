from pathlib import Path
import json

def main():
    print(little_secret())

def little_secret():
    path = Path("favorite.json")
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        return fav_num
    else:
        while(True):
            try:
                fav_num = int(input("What is your favorite number? "))
            except ValueError:
                print("Invalid input")
            else:
                contents = json.dumps(fav_num)
                path.write_text(contents)
                return fav_num
            
if __name__ == "__main__":
    main()
