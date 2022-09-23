class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        if len(nums) == 0:
            return 0
        nums.sort()
        best = 0 
        count = 0
        for i in range(N - 1):
            if nums[i + 1] - nums[i] == 1:
                count += 1
                best = max(count , best)
            elif nums[i + 1] - nums[i] == 0:
                continue
            else:
                count = 0
                
        return best + 1 
