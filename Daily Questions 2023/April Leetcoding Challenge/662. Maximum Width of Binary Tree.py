# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lookup = defaultdict(list)
        ans = 0 
        def dfs(root , depth , col):
            if not root:
                return 
            lookup[depth].append(col)
            dfs(root.left , depth + 1 , col * 2)
            dfs(root.right , depth + 1 , col * 2 + 1)

        dfs(root , 0 , 0)
        for x , y in lookup.items():
            ans = max(ans , (max(y) - min(y) + 1))
        return ans
        
