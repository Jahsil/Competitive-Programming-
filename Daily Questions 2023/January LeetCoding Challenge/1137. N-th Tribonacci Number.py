class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = {}
        def dfs(n):
            if n == 0:
                return 0
            if n in dp:
                return dp[n]

            if n == 1 or n == 2:
                return 1

            x = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            dp[n] = x
            return x

        return dfs(n)
