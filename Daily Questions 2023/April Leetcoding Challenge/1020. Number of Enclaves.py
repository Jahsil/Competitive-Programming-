class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        count , total , outOfBound = 0 , 0 , False
         

        def dfs(grid , row , col , m , n ):
            nonlocal count , outOfBound
            
            if ((row) >= 0 and (row) < m and (col) >= 0 and (col) < n) and grid[row][col] == 0:
                return 
            elif (row - 1) < 0 or (row + 1) >= m or (col - 1) < 0 or (col + 1) >= n :
                outOfBound = True
            if ((row) >= 0 and (row) < m and (col) >= 0 and (col) < n) and grid[row][col] == 1 : 
                grid[row][col] = 2
                count += 1
                dfs(grid , row + 1 , col , m , n )
                dfs(grid , row - 1 , col , m , n )
                dfs(grid , row , col + 1 , m , n )
                dfs(grid , row , col - 1 , m , n )

            return count if outOfBound == False else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 : 
                    count = 0 
                    outOfBound = False
                    total += dfs(grid , i , j , m , n)

        return total

        