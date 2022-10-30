class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        seen = set()
        
        q = deque([(0,0,0,k)])
        
        while q:
            x , y , steps , kleft = q.popleft()
            if (x , y , kleft) in seen or kleft < 0:
                continue
            if x == m - 1  and y == n - 1:
                return steps
            seen.add((x , y , kleft))
            
            if grid[x][y] == 1:
                kleft -= 1
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    q.append((nx , ny , steps + 1 , kleft))
                    
        return -1
                    
                    
            
