"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        arr = []
        
        def dfs(root):
        
        
        
            nonlocal arr
            
            if not root:
                return 
            arr.append(root.val)
            for child in root.children:
                dfs(child)
                
                
            
            return arr
        return dfs(root)
        
