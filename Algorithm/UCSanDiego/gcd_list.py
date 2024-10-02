def main():
    print("Finding GCF of two numbers")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    gcd(num1, num2)


def gcd(first, second):
    ''' GCD(a,b) the largest integer d so that d divides both a and b'''
    if(first <= second):
        least = first
    else:
        least = second
    gcd = 0

    for i in range(1, least+1):
        if(first % i == 0 and second %i == 0):
            gcd = i
    print(gcd)
if __name__ == "__main__":
    main()
