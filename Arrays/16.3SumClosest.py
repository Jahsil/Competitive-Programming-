class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[len(nums)-1]
        length = len(nums) -2
        for i in range(0 , length):
            if i == 0 or i > 0:
                start = i + 1
                end = len(nums)-1            
                while(start < end):
                    temp = nums[i] + nums[start] + nums[end]
                    if temp < target:
                        start += 1
                    else:
                        end -= 1
                        
                    if abs(temp - target) < abs(ans - target):
                        ans = temp
        return ans
      
