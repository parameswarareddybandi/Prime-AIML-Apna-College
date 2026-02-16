set1 = set()
dups = []

listLen = int(input("Enter the size of list : "))

for i in range(listLen):
    ele = int(input())
    if ele in set1:
        dups.append(ele)
    else:
        set1.add(ele)
        
print(dups)