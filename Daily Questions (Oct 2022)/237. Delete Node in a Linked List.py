# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        nodePtr = node 
        
        while nodePtr.next and nodePtr.next.next:
            nodePtr.val = nodePtr.next.val
            nodePtr = nodePtr.next
            
        nodePtr.val = nodePtr.next.val
        nodePtr.next = None
        
