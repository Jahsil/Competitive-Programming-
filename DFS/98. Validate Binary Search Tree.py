# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root , float('-inf') , float('inf'))
        
    
    def dfs(self , root , l , r):
      
        if root is None:
            return True 
        if not (root.val > l and root.val < r):
            return False
        return self.dfs(root.left , l , root.val) and self.dfs(root.right , root.val , r)
    
    
    
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        def dfs(root):
            if not root:
                return 
            nonlocal result
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            
        dfs(root)
        for i in range(1 , len(result)):
            if result[i-1] >= result[i]:
                return False
        return True
        
            
        
