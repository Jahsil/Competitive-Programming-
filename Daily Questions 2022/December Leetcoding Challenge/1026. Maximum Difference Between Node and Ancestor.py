# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = -1
        def dfs(root , maxValue , minValue):
            nonlocal ans
            if not root:
                return 
            if root.val >= maxValue:
                maxValue = root.val
            if root.val <= minValue:
                minValue = root.val
            if not root.left and not root.right:
                ans = max(ans , abs(maxValue - minValue))
            dfs(root.left , maxValue , minValue)
            dfs(root.right , maxValue , minValue)

        dfs(root , root.val , root.val)
        return ans


