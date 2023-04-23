class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        INF = 10 ** 20
        ans = INF

        has_cache = [[False] * (n + 1) for _ in range(m + 1)]
        cache = [[None] * (n + 1) for _ in range(m + 1)]

        print(has_cache)

        def dfs(i , j) : 
            if i >= m or j >= n:
                return INF
                
            if has_cache[i][j]:
                return cache[i][j]

            if i == m-1 and j == n-1:
                return grid[i][j]

            has_cache[i][j] = True
            cache[i][j] = grid[i][j] + min(dfs(i + 1 , j),dfs(i , j + 1 ))
            return cache[i][j]
         

        return dfs(0 , 0 )
        
            
