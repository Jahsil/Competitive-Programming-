class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        dd = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dd[i-j].append(mat[i][j])
                
        for i in dd:
            dd[i].sort(reverse = True)
            
        print(dd)
        for i in range(m):
            for j in range(n):
                mat[i][j] = dd[i - j].pop()
                
        return mat
