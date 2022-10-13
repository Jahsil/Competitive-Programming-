# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        nodePtr = head
        prev = None
        while nodePtr:
            if not head:
                return None
            if head.val == val:
                head = nodePtr.next
            elif nodePtr.val == val:
                prev.next = nodePtr.next
                nodePtr = nodePtr.next
                continue
                
            prev = nodePtr 
            nodePtr = nodePtr.next
            
        return head
                
                
                
            
