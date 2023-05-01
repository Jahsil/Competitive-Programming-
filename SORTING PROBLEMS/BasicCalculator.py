hashmap = dict()

nums = [3,45,6,7,7,5]
for i , n in enumerate(nums):
    hashmap[n] = i
print(hashmap)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k] == 0) :
                        if [nums[i] , nums[j] , nums[k]] not in ans:
                            ans.append([nums[i] , nums[j] , nums[k]])
        return ans