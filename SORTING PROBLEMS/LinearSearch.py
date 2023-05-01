nums = [5,4,8,5,7,1,2,9,5]
x = 77
N = len(nums)
j = 0
while j < N and x != nums[j]:
    j += 1

print(j)