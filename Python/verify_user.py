from pathlib import Path
import json
import greet_user
import username

def main():
    verify()



def verify():
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        user = str(json.loads(contents))
        n_user = input("Your username: ")
        if(user == n_user):
            print("You're our premium user")
            greet_user.greet_user()
        else:
            username.add_new_user(n_user)
            greet_user.greet_user()
            print("Thank you for becoming our new user")
                        
    else:
        print(f"Your user name is: {username.get_username()}")
            
if __name__ == "__main__":
    main()
