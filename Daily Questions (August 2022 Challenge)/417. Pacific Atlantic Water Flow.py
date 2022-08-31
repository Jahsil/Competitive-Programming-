class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def dfs(i: int, j: int, prev_height: int, coords: Set[Tuple[int]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return
            
            if (i, j) in coords:
                # already visited
                return
            
            height = heights[i][j]
            
            if height < prev_height:
                # water can't flow to a higher height
                return
            
            
            coords.add((i, j))
            
            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)
            
        pacific_coords = set()
        
       
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        
        
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)
            
        atlantic_coords = set()
            
        
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)
            
        
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
            
        
        return list(pacific_coords & atlantic_coords)
