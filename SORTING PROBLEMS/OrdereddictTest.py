from collections import OrderedDict , Counter

words = ["i","love","leetcode","i","love","coding","lamb","lamb"]
k = 1
count = (Counter(words))
print(count)
count = sorted(count.items() , key= lambda x : (-x[1] , x[0]))
result = []
for i in range(k):
    result.append(count[i][0])
print(result)


