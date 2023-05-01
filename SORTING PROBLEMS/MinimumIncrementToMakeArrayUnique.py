b_pointer = 1
a_pointer = 0
nums = [3,2,1,2,1,7]
nums.sort()
count = 0
nums.sort()
while(a_pointer < len(nums) and b_pointer < len(nums)):
    if(nums[a_pointer] == nums[b_pointer]):
        nums[b_pointer] += 1
        count += 1
        nums.sort()
    else:
        a_pointer += 1
        b_pointer += 1
print(count)