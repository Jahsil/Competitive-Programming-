class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        
        set1 , set2 , set3 = set() , set() , set()
        
        for i in range(0 , m):
            
            if i == 3 or i == 6:
                set1.clear()
                set2.clear()
                set3.clear()
            for j in range(0 , n):
                if j < 3 :
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in set1:
                        return False
                    else:
                        set1.add(board[i][j])
                        
                elif j >= 3 and j < 6 :
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in set2:
                        return False
                    else:
                        set2.add(board[i][j])
                        
                elif j >= 6:
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in set3:
                        return False
                    else:
                        set3.add(board[i][j])
                        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                
        return True
                    
            
