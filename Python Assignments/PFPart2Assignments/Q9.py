import math
num = int(input())

for i in range(2, int(math.sqrt(num)+1)):
    if num %i == 0 or num<=0:
        print("Not Prime")
        break
else:
    print("Prime")