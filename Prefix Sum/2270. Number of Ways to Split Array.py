class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        nubmerOfSplits = 0
        
        prefix = [0] * (N + 1)
        suffix = [0] * (N + 1)
        
        for i in range(N):
            prefix[i+1] = prefix[i] + nums[i]
            
        for i in range(N-1 ,-1 , -1):
            suffix[i] = suffix[i + 1] + nums[i]
     
        for i in range(N-1):
            
            left = prefix[i + 1]
            right = suffix[i + 1]
            if left >= right:
                nubmerOfSplits += 1
                
        return nubmerOfSplits
    
    
    
# Better space complexity O(1)
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        nubmerOfSplits = 0
        
        total = sum(nums)
        left = 0
        
        for i in range(N-1):
            left += nums[i]
            right = total - left
            
            if left >= right:
                nubmerOfSplits += 1
                
        return nubmerOfSplits
            
