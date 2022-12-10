# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        def total(root):
            if not root:
                return 0
            return root.val + total(root.left) + total(root.right)

        tot = total(root)
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            x = root.val + dfs(root.left) + dfs(root.right)
            y = tot - x

            res = max(res , x * y)
            return x

        dfs(root)
        return res % MOD

        
