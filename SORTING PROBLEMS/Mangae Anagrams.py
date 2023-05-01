import collections

arr = [2,1,3,1,2,3,3]
ans = [4,2,7,2,4,4,5]
print(arr , "===" , ans)
N = len(arr)
c = collections.defaultdict(list)
res = []

for i in range(N):
    c[arr[i]].append(i)
print(c)
for i , num in enumerate(arr):
    tmp = []
    for v in c[num]:
        if i != v:
            tmp.append(abs(i - v))
        else:
            continue
    res.append(sum(tmp))
print(res)





