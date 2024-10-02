def main():
    num = int(input("Number: "))
    print(f"Fibonacci of {num} = {fibonacci_recursive(num)}")
    


def fibonacci_recursive(n):
    ''' This is a naive algorithm. it takes much time, T(n) >= F(n)'''
    if(n <= 1):
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))
if __name__ == "__main__":
    main()
