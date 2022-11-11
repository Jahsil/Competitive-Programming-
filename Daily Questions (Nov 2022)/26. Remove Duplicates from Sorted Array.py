class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        start = 0 
        
        for end in range(N):
            if nums[end] > nums[start]:
                #print(nums[end] , nums[s])
                nums[start + 1] = nums[end]
                start += 1
                
                
        return start + 1
