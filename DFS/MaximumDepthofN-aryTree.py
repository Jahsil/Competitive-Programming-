"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maximum = 0
        if not root:
            return 0
        def dfs(root , counter): 
            if not root.children:
                return 
            self.maximum = max(self.maximum , counter)
            for child in root.children:
                dfs(child , counter + 1)
        dfs(root , 1)
        return self.maximum + 1
