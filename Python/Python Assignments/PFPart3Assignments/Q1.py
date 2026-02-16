str = input("Enter a string: ")
revstr = str[::-1]
if str == revstr:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")