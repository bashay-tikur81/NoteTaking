from pathlib import Path

def main():
    path = Path("pi_million_digits.txt")
    contents = path.read_text()
    pi_string = ''
    for line in contents.splitlines():
        pi_string += line.strip()
        
    birthday = input("Write your birth dat in ddmmyyyy format: ")
    if birthday in pi_string:
        print("your birth date appears on million digits of pi")
    else:
        print("You birth date isn't on the million digits of pi")
        
    print(f"{pi_string[:50]} ...")
    print(len(pi_string))

if __name__ == "__main__":
    main()
