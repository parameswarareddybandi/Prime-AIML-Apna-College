salary = int(input("Enter Salary  : "))

if salary < 30000:
    print("Final Tax Rate : ", 0.05 * salary)
elif salary > 30000 and salary <= 70000:
    print("Final Tax Rate : ", 0.15 * salary)
else:
    print("Final Tax Rate : ", 0.25 * salary)