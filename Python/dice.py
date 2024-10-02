from random import randint
class Dice:
    def __init__(self):
        self.sides = []
        self.sides.append(".")
        self.sides.append(":")
        self.sides.append(":.")
        self.sides.append("::")
        self.sides.append("::.")
        self.sides.append(":::")
    def roll_over(self):
        chosen = randint(0,5)
        print(self.sides[chosen])
       # print(choice(self.sides))


def main():
    dice1 = Dice()
    dice1.roll_over()
    
if __name__ == "__main__":
      main()
      
