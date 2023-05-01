nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)

for i in range(N-1):
    minIndex = i
    for j in range(i , N):
        if nums[j] <= nums[minIndex]:
            minIndex = j
    nums[i] , nums[minIndex] = nums[minIndex] , nums[i]

print(nums)
