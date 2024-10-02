from pathlib import Path

def main():
    path = Path("cats.txt")
    try:
        
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"{path} was not found")
        pass                    # do nothing, just ignore the exception
    else:
        print(contents.strip())
    

if __name__ == "__main__":
    main()
