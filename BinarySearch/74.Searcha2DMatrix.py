# Solution 1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0]) - 1

        
       
        for i in range(m):
            start = 0 
            while(start <= n):
                mid = start + (n - start)//2
                if matrix[i][mid] == target:
                    print('hello')
                    return True
                elif matrix[i][mid] > target:
                    n = mid - 1
                else:
                    start = mid + 1
        return False

# Solution 2

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        start = 0 
        end = (row * col) - 1
        
        while(start <= end):
            mid = start + (end - start)//2
            middle = matrix[mid//col][mid%col]
            if middle == target:
                return True
            elif middle > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
