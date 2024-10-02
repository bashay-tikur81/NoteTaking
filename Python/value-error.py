def main():
    """" Handling ValueError when adding two numbers """
    while(input("'q' for quit, else for continue: ").lower() != 'q'):
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        if(num1 == 'q'):
            break
        elif(num2 == 'q'):
            break

        try:
            sum = int(num1) + int(num2)
        except ValueError:
            print("Not valid number(s)!")
        else:
            print(f"Sum = {sum}")

if __name__ == "__main__":
    main()
