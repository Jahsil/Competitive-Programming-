class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        def paths(m , n):
            if m == 1 and n == 1:
                return 1
            if m <= 0 or n <= 0:
                return 0
            if (m , n) in dp:
                return dp[(m , n)]
            
            dp[(m , n)] = paths(m - 1 , n) + paths(m , n - 1)
            return dp[(m , n)]
        
        return paths(m , n)
