import name_function

def main():
    print("Type 'q' to quit at any time")
    while(True):
        first = input("First name: ")
        if(first == 'q'):
            break
        last = input("Last name: ")
        if(last == 'q'):
            break

        formatted_name = name_function.get_formatted_name(first, last)
        print(f"\tNeatly formatted name is {formatted_name}")

if __name__ == "__main__":
    main()
