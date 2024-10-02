def main():
    print("Finding GCD of the following numbers")
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(f"{gcd_Euclidean(num1, num2)}")

def gcd_Euclidean(a,b):
    '''This is an efficient algorithm in O(log(n))
       each time it divides the problem in two.
       In order to have an efficient algorithm you need to know somthing
       different than the trivial ones'''
    if(b == 0):
        return a
    else:
        r = a%b
        return gcd_Euclidean(b,r)
        
if __name__ == "__main__":
    main()
