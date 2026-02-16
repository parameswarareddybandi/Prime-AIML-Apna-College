set1 = set()
set2 = set()

len1 = int(input("Enter the length of list 1 : "))
len2 = int(input("Enter the length of list 2 : "))
 
for i in range(len1):
    set1.add(int(input()))
    
for i in range(len2):
    set2.add(int(input()))

common = set1.intersection(set2)

if len(common) == 0:
    print("No Common Elements")
else:
    print(common)

