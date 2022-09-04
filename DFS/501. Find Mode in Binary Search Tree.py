# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        d = dict()
        
        def dfs(root):
            if not root:
                return 
            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        d = sorted(d.items() , key=operator.itemgetter(1))
        arr = []
        for x , y in d:
            if y == d[-1][1]:
                arr.append(x)     
        return arr
        
       
        
