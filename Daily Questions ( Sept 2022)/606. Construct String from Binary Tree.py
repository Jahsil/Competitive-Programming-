# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = []
        
        def dfs(root):
            nonlocal arr
            if not root:
                return 
            
            arr.append(f"{root.val}")
            if not root.left and root.right:
                arr.append(f"()")
            
            if root.left:
                
                arr.append("(")
                dfs(root.left)
                arr.append(")")
            if root.right:
                
                arr.append("(")
                dfs(root.right)
                arr.append(")")
            return arr
            
        dfs(root)
        return "".join(arr)
