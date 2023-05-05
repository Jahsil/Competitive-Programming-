# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        def dfs(root , tmp):
            nonlocal maxVal
            if not root:
                return 

            tmp[root.val] = not tmp[root.val]
            if not root.left and not root.right:
                if sum(tmp) <= 1:
                    maxVal += 1
            dfs(root.left , tmp)
            dfs(root.right , tmp)
            tmp[root.val] = not tmp[root.val]

        dfs(root , [False] * 10)
        return maxVal
