nums = [5,4,8,5,7,1,2,9,5]
N = len(nums)
print(nums)
for i in range(1 , N):
    temp = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > temp:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j+1] = temp

print(nums)


