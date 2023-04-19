# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLength = 0 

        def dfs(root , depth , state):
            nonlocal maxLength
            if not root:
                return 
            maxLength = max(maxLength , depth )

            if root.left:
                if state == "left":
                    dfs(root.left , 1 , "left")
                else:
                    dfs(root.left , depth + 1 , "left")
            if root.right:
                if state == "right":
                    dfs(root.right , 1 , "right")
                else:
                    dfs(root.right , depth + 1 , "right")
            
            return maxLength

        return dfs(root , 0 , "")
        
