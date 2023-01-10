# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr = []
        def dfs(root):
            nonlocal arr
            if not root:
                arr.append(root)
                return 
            
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(p)
        parr = arr
        arr = []
        dfs(q)
        qarr = arr
        return parr == qarr

