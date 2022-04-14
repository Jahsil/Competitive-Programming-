# Recursive Solution 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root , result)
        return result
        
    def dfs(self , root , result):
        if root is not None:
            self.dfs(root.left , result)
            result.append(root.val)
            self.dfs(root.right , result)
            
            
            
# Iterative Solution using Stack 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        nodePtr = root
        while nodePtr is not None or stack != []:
            while nodePtr is not None:
                stack.append(nodePtr)
                nodePtr = nodePtr.left 

            currentNode = stack.pop()
            result.append(currentNode.val)
            nodePtr = currentNode.right

        return result
        
            


        
