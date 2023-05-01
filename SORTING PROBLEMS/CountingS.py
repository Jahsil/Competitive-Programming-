nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)
count = [0] * (max(nums) + 1)
print(count)
ans = [0] * N

for i in range(N):
    count[nums[i]] += 1

print(count)
for i in range(1 , len(count)):
    count[i] += count[i - 1]
print(count)
for i in range(N-1 , -1 , -1):
    ans[count[nums[i]] - 1] = nums[i]
    count[nums[i]] -= 1
print(ans)