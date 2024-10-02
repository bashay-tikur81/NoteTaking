from pathlib import Path
import json
import favorite_number

def main():
    path = Path("usernames.json")
    user_data = {}
    if path.exists():
        contents = path.read_text()
        user = str(json.loads(contents)).strip("{}")
        username, fav_num = user.split(":")
        print(f"Username: {username.strip("''")}")
        print(f"Favorite number: {fav_num}")
    else:
        username = input("username: ")
        fav_num = favorite_number.little_secret()
        user_data[username] = fav_num
        contents = json.dumps(user_data)
        path.write_text(contents)
        print(f"{username} your favorite number is {fav_num}")
        
    
if __name__ == "__main__":
    main()
