nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)
print(nums)
for i in range(N):
    for j in range(0 , N - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j] , nums[j+1] = nums[j+1] , nums[j]

print(nums)