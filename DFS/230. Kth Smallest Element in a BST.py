# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
         
        def dfs(root , arr , k):
            if not root :
                return 
            dfs(root.left , arr , k)
            arr.append(root.val)
            dfs(root.right ,arr , k)
            
            return arr
        
        arr = dfs(root , arr , k)
        return arr[k-1]
