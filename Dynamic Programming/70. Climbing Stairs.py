class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def recursion(m):
            if m > n:
                return 0
            if m == n:
                return 1 
            if m in dp:
                return dp[m]
            dp[m] = recursion(m + 1) + recursion(m + 2)
            
            return dp[m]
        return recursion(0)
        
