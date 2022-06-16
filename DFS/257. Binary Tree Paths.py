# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        arr = []
        
        def dfs(root , path ):
            nonlocal arr
            newPath = path + str(root.val) + "->"
            
            if root.left:
                dfs(root.left , newPath )
            if root.right:
                dfs(root.right , newPath )
                
            if not root.left and not root.right:
                arr.append(newPath.removesuffix('->'))
                
        dfs(root , "")
        return arr
        
