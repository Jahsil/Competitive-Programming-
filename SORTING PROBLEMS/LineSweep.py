from sortedcontainers import SortedList

arr = SortedList()
ls = [(2 , 5) , (4 , 8) , (9 , 12)]
for s , e in ls:
    arr.add((s , -1))
    arr.add((e , 1))

result = 0
maxResult = 0
curr = arr[0][0]
counter = 0

for s ,e in arr:
    if counter == 0:
        maxResult = max(maxResult , result)
    if counter > 0:
        result += s - curr
        curr = s
        print(result , curr , counter)
    if e == -1:
        counter += 1
    else:
        counter -= 1








print(ls)
print(arr)
print(result)
print('maxResult' , maxResult)