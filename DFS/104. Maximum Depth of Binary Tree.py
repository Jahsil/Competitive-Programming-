# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.height = 0 
        depth = 1
        def dfs(root , depth):
            
            if not root:
                return 
            if not root.left and not root.right:
                self.height = max (self.height , depth)
                
            dfs(root.left , depth + 1)
            dfs(root.right , depth + 1)
            
            
        dfs(root , depth)
        return self.height        
           
