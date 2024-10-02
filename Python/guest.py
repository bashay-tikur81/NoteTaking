from pathlib import Path

def main():
    cont = 1
    path = Path("guest.txt")
    names = ''
    while(cont):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        names += f"{first_name } | {last_name}\n"
        path.write_text(names)
        cont = int(input("Write '1' to continue and '0' to quit: "))
        
    print(path.read_text())
    

if __name__ == "__main__":
    main()
