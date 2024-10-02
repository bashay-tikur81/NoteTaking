def main():
    '''Catching ZeroDivionErro and continuing the program run'''
    print("Give me two numbers and I will divide them.")
    print("Type 'q' to quite the program")
    while(True):
        num1 = input("First number: ")
        if(num1 == 'q'):
            break
        num2 = input("Second number: ")
        if(num2 == 'q'):
            break
        try:
            result = int(num1)/int(num2)
            print(result)
        except (ZeroDivisionError, ValueError):
            print("Something went wrong")
    


if __name__ == "__main__":
    main()
