# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = dict()
        def dfs(root , row , col , level):
            if not root:
                return 
            if col in d:
                d[col].append((level , root.val))
            else:
                d[col] = [(level , root.val)]
            if root.left:
                dfs(root.left , row + 1 , col -1 , level + 1)
            if root.right:
                dfs(root.right , row + 1 , col + 1 , level + 1)
                
        dfs(root , 0 , 0 , 0)  
        d = sorted(d.items() , key=operator.itemgetter(0))
        arr = []
        for x , y in d:
            tmp = []
            for index , tup in enumerate(sorted(y , key = lambda t: (t[0] , t[1]))):
                tmp.append(tup[1])
            arr.append(tmp)     
        return arr
                
            
# Better approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = defaultdict(list)
        
        def dfs(root , x , y):
            if not root:
                return 
            lookup[(x,y)].append(root.val)
            dfs(root.left , x + 1 , y -1)
            dfs(root.right , x + 1 , y + 1)
            
        dfs(root , 0 , 0)
        cols = defaultdict(list)
        for x , y in sorted(lookup.keys()):
            cols[y].extend(sorted(lookup[(x,y)]))
        arr = []
        for x in sorted(cols.keys()):
            arr.append(cols[x])
            
        return arr
            
        
