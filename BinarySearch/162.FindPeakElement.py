class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 2

        while(start <= end):
        
            mid = start + (end - start)//2
            if nums[mid -1] < nums[mid] and nums[mid] > nums[mid +1]:
                return mid
            elif nums[mid -1] < nums[mid] and nums[mid +1] > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        start = 0
        end = len(nums) - 1     
        if nums[start] > nums[end]:
            return start
        else:
            return end
  
     # Easy solution
    
    class Solution:
        def findPeakElement(self, nums: List[int]) -> int:
            start, end = 0, len(nums)-1

            while start < end:
                mid = start + (end - start)//2
                if nums[mid] > nums[mid+1]:
                    end = mid
                else:
                    start = mid + 1

          return start
          
            
        
