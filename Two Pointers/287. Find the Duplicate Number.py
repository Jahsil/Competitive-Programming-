class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        N = len(nums)
        a = 0
        b = 1
        
        while a < N and b < N:
            if nums[a] == nums[b]:
                return nums[a]
            else:
                a += 1
                b += 1
