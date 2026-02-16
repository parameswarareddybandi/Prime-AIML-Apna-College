 
arr = [1, 2, 3, 4 ,5 , 6, 7, 8, 9]
tempEven = []
tempOdd = []
for ele in arr:
    if ele%2 == 0:
        tempEven.append(ele)
    else:
        tempOdd.append(ele)

evenTuple = tuple(tempEven)
oddTuple = tuple(tempOdd)

print(evenTuple)
print(oddTuple)
