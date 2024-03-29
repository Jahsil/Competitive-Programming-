# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        result = float('inf')
        def dfs(root):
            nonlocal prev , result
            if not root:
                return 
            dfs(root.left)
            result = min(result , root.val - prev)
            prev = root.val
            dfs(root.right)
            
            return result
        return dfs(root)
        
        
        
#using extra space 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
            
        dfs(root)
        return min(arr[i] - arr[i-1] for i in range(1 , len(arr)))
   
