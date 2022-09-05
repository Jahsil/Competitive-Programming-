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
        def dfs(root , arr):
            if not root:
                return 
            arr.append(root.val)
            for child in root.children:
                dfs(child , arr)
            return arr
        dfs(root , arr)
        return arr
