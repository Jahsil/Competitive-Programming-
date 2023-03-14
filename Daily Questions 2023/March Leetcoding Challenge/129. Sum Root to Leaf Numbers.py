# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root , path):
            if not root:
                return 
            tmp = path + [str(root.val)]

            if not root.left and not root.right:
                arr.append(tmp)
            dfs(root.left , tmp)
            dfs(root.right , tmp)

        dfs(root , [])
        return sum(int("".join(i)) for i in arr) 
