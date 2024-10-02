class Dog:
    def __init__(self, name, age):
        """ Initialize name and age attribute """
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def rollover(self):
        print(f"{self.name} is now rolling.")



def main():
    Dog bob = new(Dog)
    bob.sit()






if __name__ == "__main__":
    main()
