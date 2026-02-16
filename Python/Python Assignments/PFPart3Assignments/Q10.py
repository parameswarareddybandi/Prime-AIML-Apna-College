str = input("Enter a string : ")
unique = set()

for i in range(len(str)):
    unique.add(str[i])

print(unique)
print("There are ",len(unique)," unique letters.")