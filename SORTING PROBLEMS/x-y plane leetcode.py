import math

points = [[3,3],[5,-1],[-2,4]]
k = 2
origin = 0
result = [( x , y ,  math.sqrt((x - origin) ** 2 + (y - origin) ** 2) )for x , y in points]

print(result)
ans = []
i = 0
for x , y , d in sorted(result , key = lambda x : x[2]):
    if i < k:
        ans.append([x , y])
        i += 1
    else:
        break

print(ans)
