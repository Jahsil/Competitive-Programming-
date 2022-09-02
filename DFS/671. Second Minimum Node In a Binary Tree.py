# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root , minValue):
            nonlocal arr
            if not root:
                return    
            minValue = min(minValue , root.val)
            if root.val > minValue:
                arr.append(root.val)
            
            dfs(root.left , minValue )
            dfs(root.right , minValue )
            
            return arr
        dfs(root , root.val)
        return min(arr) if len(arr) > 0 else -1
