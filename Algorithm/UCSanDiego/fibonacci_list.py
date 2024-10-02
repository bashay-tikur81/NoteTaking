def main():
    num = int(input("Number: "))
    print(f"Fibonacci of {num} = {fibonacci_list(num)}")

def fibonacci_list(num):
    ''' An efficient program '''
    fib_array = []
    fib_array.append(0)
    fib_array.append(1)
    if(num > 1):
        for i in range(2,num+1):
            fib_array.append(fib_array[i-1] + fib_array[i-2])

    return fib_array[num]


if __name__ == "__main__":
    main()
