class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        result[0] = self.firstPosition(nums , target)
        result[1] = self.lastPosition(nums , target)
        return result
    
    def firstPosition(self , nums , target):
        index = -1
        start = 0 
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            if (nums[mid] >= target):
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == target :
                index =  mid 
                
        return index
    def lastPosition(self , nums , target):
        index = -1
        start = 0 
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            if (nums[mid] <= target):
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target :
                index =  mid 
                
        return index
