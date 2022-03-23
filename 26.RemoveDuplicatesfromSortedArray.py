class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            j = i + 1
            while(j < len(nums) and nums[i] == nums[j]):
                nums.pop(j)
                
                
                
 # O(n) solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for index in range(1,len(nums)):
            if(nums[index] != nums[index-1]):
                k+=1
                nums[k] = nums[index]
        return k+1
