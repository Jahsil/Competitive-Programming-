# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root , summ , targetSum):
            if root is not None:
                summ += root.val
                if not root.left and not root.right and summ == targetSum:
                    return True
                return dfs(root.left , summ , targetSum) or dfs(root.right , summ , targetSum)
            else:
                return False
            
        return dfs(root , 0 , targetSum)
        
                
        
