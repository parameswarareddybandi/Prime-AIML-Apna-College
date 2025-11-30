num = int(input("Enter a number : ")) #number
numstr = str(num) #string
for val in numstr:
    print(val)

    #or

while (num > 0):
    digit = int(num%10)
    print(digit)
    num = int(num/10)
