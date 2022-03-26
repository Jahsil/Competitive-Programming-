class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1
        
        while(start < end):
            mid = start + (end - start)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
    
    
    # An alternative solution
    
    class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
    
        while start <= end:
            mid = start + (end - start)//2
        
            if(nums[mid - 1] > nums[mid]): 
                return nums[mid]
            elif(nums[mid] > nums[end]): 
                start = mid + 1 
            else: 
                end = mid - 1
        return nums[mid]
