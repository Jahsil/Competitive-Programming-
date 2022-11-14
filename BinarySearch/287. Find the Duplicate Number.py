class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            count = 0
            
            count = sum(num <= mid for num in nums)
            if count > mid:
                dup = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return dup
            
