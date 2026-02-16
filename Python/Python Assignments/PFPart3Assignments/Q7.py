str = input("Enter a string with spaces : ")
count = 0
for i in range(len(str)):
    if str[i] == " ":
        count += 1

print("Spaces : ",count)