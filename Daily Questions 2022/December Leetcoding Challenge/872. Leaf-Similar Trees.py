# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr  = [] 
        def dfs(root):
            nonlocal arr
            if not root:
                return 
            if not root.left and not root.right:
                arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root1)
        a = arr
        arr = []
        dfs(root2)
        b = arr
        return a == b

        
