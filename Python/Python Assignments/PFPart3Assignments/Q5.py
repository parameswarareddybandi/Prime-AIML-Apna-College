students = {
    "Paramesh" : 99,
    "Upendra" : 90,
    "Pardhu" : 91
}
print('''
A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks ''')
op = input("Enter a value : ")

def addStudent():
    name = input("Student Name : ")
    marks = int(input("Marks : "))
    students[name] = marks
    print(students)

def updateMarks():
    name = input("Student Name : ")
    if students.get(name):
       marks = int(input("Enter marks : "))
       students.update({name : marks})
       print("Marks Updated : ",students)
    else:
        print("Student data not found.")
        print(students)

def searchStudent():
    name = input("Student Name : ")
    if students.get(name):
        print("Student Data found : ",name,students.get(name))
    else:
        print("Student data not found")
        
def displayData():
    for name in students.keys():
        print(name, students.get(name))
        
match op:
    case "A":
        addStudent()
    case "B":
        updateMarks()
    case "C":
        searchStudent()
    case "D":
        displayData()
    case "_":
        print("Wrong Input")