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
            
            
            
            
            
            
            
            
            
            
