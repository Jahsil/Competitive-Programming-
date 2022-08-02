class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        numOfIslands = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.dfs(grid , i , j , row , col)
                    numOfIslands += 1
                    
        return numOfIslands
    
    def dfs(self , grid , x , y , row ,col):
        if x < 0 or x >= row or y < 0 or y >= col or grid[x][y]!="1":
            return
        
        grid[x][y] = "2"
        
        self.dfs(grid , x  , y + 1 , row , col)
        self.dfs(grid , x + 1 , y , row , col)
        self.dfs(grid , x  , y - 1 , row , col)
        self.dfs(grid , x - 1 , y , row , col)
        
        
                    
