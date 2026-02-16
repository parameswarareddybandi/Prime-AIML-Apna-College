num = int(input("Enter a number : "))

sum = 0
while num>0:
    temp = int(num % 10)
    sum += temp
    num = int(num/10)

print("Sum of the digits of the given number : ", sum)