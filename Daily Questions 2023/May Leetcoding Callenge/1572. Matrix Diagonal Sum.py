class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
       
        for i in range(m):
            for j in range(n):
                if i == j:
                    ans += mat[i][j]
                elif i != j and i + j == m - 1:
                    ans += mat[i][j]
        

        return ans
