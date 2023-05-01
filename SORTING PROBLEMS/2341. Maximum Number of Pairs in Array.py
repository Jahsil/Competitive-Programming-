import collections

nums = [0]
nums.sort()
print(nums)
pairsRemoved = 0
numbersLeft = 0
N = len(nums)
i = 0
count = collections.Counter(nums)
print(count)
for x , y in count.items():
    while count[x] >= 2:
        count[x] -= 2
        pairsRemoved += 1

for x , y in count.items():
    if count[x] != 0:
        numbersLeft += 1

print([pairsRemoved , numbersLeft])