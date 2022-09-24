# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        
        def traverse(root , current):
            nonlocal result
            if not root:
                return 
            
            if current + root.val == targetSum:
                result += 1
                
            traverse(root.left , current + root.val)
            traverse(root.right , current + root.val)
            
            
                
        def dfs(root):
            if not root:
                return 
            traverse(root , 0)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return result
