
def main():
    age: int = int(input("What is your age: "))
    age_days: int = age_in_days(age)
    print(f"Your are {age_days} days years old")

def age_in_days(age: int) -> int:
    return age*365


if __name__ == "__main__":
    main()

    
