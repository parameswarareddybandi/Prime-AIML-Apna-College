while True:
    num = input()

    if num == "Quit":
        break

    num = float(num)
    if num == 0:
        print("Zero")
    elif num > 0:
        print("Positive")
    else:
        print("Negative")