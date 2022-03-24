class Solution:
    def swap(self , nums , i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def reverseNums(self , nums , start , end):
        while start < end:
            self.swap( nums , start , end)
            start += 1
            end -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums , 0 , 1)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        self.reverseNums(nums , i + 1 , len(nums) -1)
        if i == -1:
            return 
        num = i + 1
        while num < len(nums) and nums[num] <= nums[i]:
            num += 1
        self.swap(nums , num , i)
  
        
