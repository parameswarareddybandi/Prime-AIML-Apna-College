size = int(input("Enter the size of an array: "))
arr = []
print("Enter the elements of the array: ")
for i in range(size):
    ele = int(input())
    arr.append(ele)

print("Average of the array is: ", sum(arr) / size)