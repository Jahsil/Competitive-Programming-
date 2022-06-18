# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        finalSum = 0 
        
        def dfs(root , path , sm ):
            nonlocal arr , finalSum
            
            sm += root.val
            tmp = path + [root.val]
            
            if root.left:
                dfs(root.left , tmp , sm)
            if root.right:
                dfs(root.right , tmp , sm)
                
            if not root.left and not root.right:
                arr.append(tmp)
                num = [str(integer) for integer in tmp]
                _string = "".join(num)
                finalSum += int(_string)
                
                
                
        dfs(root , [] , 0)
        return finalSum 
