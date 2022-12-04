class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * N 
        prefix[0] = nums[0]
        for i in range(1 , len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        ans = [0] * N
        start = 0
        end = len(prefix) - 1
        prev = 1
        for i in range(len(prefix)):
            if prev != len(prefix):
                ans[i] = abs((prefix[i] // prev ) -
                             (prefix[end] - prefix[start]) // (len(prefix) - prev))
                prev += 1
                start += 1
        ans[-1] = prefix[-1] // len(prefix)    
        minValue = min(ans)
        return ans.index(minValue)
            
        
        
        
# much faster solution
        
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        
        prefix = [0] * (N + 1)
        suffix = [0] * (N + 1)
        
        for i in range(N):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(N - 1 , - 1 , -1):
            suffix[i] = suffix[i+1] + nums[i]
 
        minIndex = 0
        minValue = float('inf')
        
        for i in range(N):
            
            left = prefix[i + 1]
            left //= i + 1
            
            right = suffix[i + 1]
            if (N - i - 1) != 0:
                right //= N - i - 1
                
            diff = abs(left - right)
            
            if diff < minValue:
                minValue = diff
                minIndex = i
                
        return minIndex
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
