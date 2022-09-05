"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = defaultdict()
        def dfs(root , level):
            if not root:
                return 
            if level in d:
                d[level].append(root.val)
            else:
                d[level] = [root.val]
            for child in root.children:
                dfs(child , level + 1 )               
        dfs(root , 0)
        arr = []
        for x in d.values():
            arr.append(x) 
        return arr
