class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        minOperations = 0
        N = len(nums)
        
        for i in range(N):
            if nums[i] == 0:
                continue
            else:
                num = nums[i]
                for i in range(i , N):
                    nums[i] -= num
                minOperations += 1
                
        return minOperations
                    
        
# Using a hash set 

class Solution:
   def minimumOperations(self, nums: List[int]) -> int:
       return len(set(x for x in nums if x > 0))
                    
        
