# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = -1001

        def dfs(root):
            nonlocal maxVal
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            l = max(l , 0)
            r = max(r , 0)
            maxVal = max(maxVal , root.val + l + r)
            print(maxVal , l , r)
            return root.val + max(l , r)
            
        dfs(root)
        return maxVal


