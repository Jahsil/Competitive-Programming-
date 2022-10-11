class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        hi = nums[-1] * nums[-2] * nums[-3]
        lo = nums[0] * nums[1] * nums[-1]
        
        return max(hi , lo)
