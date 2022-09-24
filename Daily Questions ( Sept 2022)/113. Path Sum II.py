# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr = []
        
        def dfs(root , path ,currentSum):
            nonlocal arr
            if not root:
                return 
            currentSum += root.val
            tmp =  path + [root.val]
            if root.left:
                dfs(root.left , tmp , currentSum)
            if root.right:
                dfs(root.right , tmp , currentSum)
            
            if currentSum == targetSum and not root.left and not root.right :
                arr.append(tmp)
            
            return arr
        
        return dfs(root , [] , 0)
