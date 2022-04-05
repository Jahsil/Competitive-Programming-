class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1 :
            return nums[0]
        
        currentSum = sum(nums[0:k])
        maxSum = currentSum
        
        for end in range(k , len(nums)):
            currentSum -= nums[end - k]
            currentSum += nums[end]
            
            if currentSum >= maxSum :
                maxSum = currentSum 
                
        return maxSum / k
 


# An Alternative Solution

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0 
        currentSum = 0
        maxAverage = float('-inf') 
        
        if len(nums) == 1:
            return nums[0]
        
        for end in range(len(nums)):
            currentSum += nums[end]
            
            if end - start + 1 == k : 
                maxAverage = max ( maxAverage , currentSum / k)
                currentSum -= nums[start]
                start += 1
                
        return maxAverage
            
            
        
            
            
            
        
