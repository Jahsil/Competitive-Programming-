# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodePtr = head
        result = []
        while nodePtr:
            result.append(nodePtr.val)
            nodePtr = nodePtr.next
        
        if result == result[::-1]:
            return True 
        else:
            return False
        
