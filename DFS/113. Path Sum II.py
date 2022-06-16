# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr = []
         
        def dfs(root , path ,  currentSum):
            nonlocal arr
            
            currentSum += root.val
            newArr = path + [root.val]
            
            if root.left:
                dfs(root.left , newArr , currentSum)
            if root.right:
                 dfs(root.right , newArr , currentSum)
           
            if not root.left and not root.right and currentSum == targetSum:
                arr.append(newArr)
                
        if not root:
            return []
        dfs(root , [] , 0)
        return arr
                
                
            
            
      
            
