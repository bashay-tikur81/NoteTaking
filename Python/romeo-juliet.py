from pathlib import Path

def main():
    path = Path("romeo-juliet.txt")
    contents = path.read_text(encoding='utf-8')
    words = contents.split()
    i,romeo,juliet,love = 0,0,0,0
    while(i < len(words)):
        if(words[i].lower() == "romeo"):
            print(words[i], end = ',')
            romeo += 1
        elif(words[i].lower() == "juliet"):
            print(words[i], end = ',')
            juliet += 1
        elif(words[i].lower() == "love"):
            print(words[i], end = ',')
            love += 1
        i+=1
        
    print(f"\nJuliet was called: {juliet} times")
    print(f"Whereas Romeo was called: {romeo} times")
    print(f"Love is written: {love} times in the play.")

if __name__ == "__main__":
    main()
