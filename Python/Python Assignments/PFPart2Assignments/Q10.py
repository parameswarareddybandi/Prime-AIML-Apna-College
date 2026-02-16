import random

mine = random.randint(1,100)

while True:
    num = int(input("Enter a number between 1 and 100 : "))
    if num > mine:
        print("Too high")
    elif num < mine:
        print("Too low")
    else:
        print("Correct!")
        break    