# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(root , dep):
            if not root:
                return 
            if dep == depth and depth == 1:
                node = TreeNode()
                node.val = val
                node.left = root
                root = node
                
            if dep == (depth - 1):
                l , r= TreeNode() , TreeNode()
                l.val = val
                r.val = val
                ltmp = root.left
                rtmp = root.right
                root.left = l
                root.right = r
                l.left = ltmp
                r.right = rtmp
                
                
            dfs(root.left , dep + 1)
            dfs(root.right , dep + 1)
            
            return root
        
        return dfs(root , 1)
