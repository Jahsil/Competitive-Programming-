class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(n):
            for j in range(n):
                x = matrix[i][j]
                
                if x in rows[i]:
                    return False
                if x in cols[j]:
                    return False
                
                rows[i].add(x)
                cols[j].add(x)
                
        return True
