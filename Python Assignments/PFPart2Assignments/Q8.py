a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
op = input("Enter operation : ")

def calculator(a, b, op):
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        
res = calculator(a, b, op)
print(res)