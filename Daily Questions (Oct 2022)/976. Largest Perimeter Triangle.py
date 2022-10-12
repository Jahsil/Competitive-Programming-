class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort(reverse = True)
        a , b , c = nums[0] , nums[1] , nums[2]
        for i in range(0 , N): 
            if  a + b > c and a + c > b and b + c > a:
                return a + b + c
            else:
                if i + 3 <= N - 1:
                    a , b , c = nums[i + 1] , nums[i + 2] , nums[i + 3]    
        return 0
