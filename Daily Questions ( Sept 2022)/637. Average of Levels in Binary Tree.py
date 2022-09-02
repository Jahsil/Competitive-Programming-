# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = {}
        arr = []
        
        def dfs(root , depth):
            nonlocal levels
            if not root:
                return 
            if depth in levels:
                levels[depth].append(root.val)
            else:
                levels[depth] = [root.val]
                
            dfs(root.left , depth + 1)
            dfs(root.right , depth + 1)
            
        dfs(root , 0)
        print(levels)
        
        for vals in levels.values():
            arr.append(sum(vals)/len(vals))
        return arr

            
