class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def recursion(index , targetSum):
            if index == len(nums):
                return 1 if target == targetSum else 0
            if (index , targetSum) in dp:
                return dp[(index , targetSum)]
            dp[(index , targetSum)] = recursion(index + 1 , targetSum + nums[index])+recursion(index + 1 , targetSum - nums[index])
            
            return dp[(index , targetSum)]
        
        return recursion(0 , 0)
