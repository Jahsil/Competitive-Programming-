
#  USING 2 FOR LOOPS : TIME COMPLEXITY : O(N2)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target and i!= j:
                    ans.append(i)
                    ans.append(j)
                    return ans


# USING HASHMAP : TIME COMPLEXITY : O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i , num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return[hashmap[difference] , i]
            hashmap[num] = i



