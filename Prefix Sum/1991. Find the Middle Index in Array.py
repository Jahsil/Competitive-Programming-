class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * (N + 1)
        suffix = [0] * (N + 1)
        
        for i in range(N):
            prefix[i+1] = prefix[i] + nums[i]
            
        for i in range(N-1 ,-1 , -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(1 , N+1):
            if (prefix[i-1] == suffix[i]):
                return i-1
        return -1
