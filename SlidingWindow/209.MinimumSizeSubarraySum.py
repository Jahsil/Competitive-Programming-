class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        currentSum = 0 
        start = 0 
        
        for i in range(len(nums)):
            currentSum += nums[i]
            while currentSum >= target:
                result = min(result , i - start + 1)    
                currentSum -= nums[start] 
                start += 1  
            
           
        if result < float('inf'):
            return result 
        else:
            return 0
