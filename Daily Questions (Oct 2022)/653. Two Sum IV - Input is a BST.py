# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        def dfs(root):
            nonlocal nums
            if not root:
                return 
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
            
            return nums
        dfs(root)
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] + nums[end] == k:
                return True
            if nums[start] + nums[end] > k:
                end -= 1
            else:
                start += 1
        return False
            
# Using a hash set but slower solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        
        def dfs(root):
            if not root:
                return False
            diff = k - root.val
            if diff in s:
                return True
            else:
                s.add(root.val)
                
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
