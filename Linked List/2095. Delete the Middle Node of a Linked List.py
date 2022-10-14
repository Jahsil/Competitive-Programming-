# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        nodePtr = head
        
        while nodePtr:
            nodePtr = nodePtr.next
            length += 1
        if not head.next:
            return None
        nodePtr = head
        prev = None
        i = 0
        while nodePtr:
            if not head:
                return None
            if i < length//2:
                prev = nodePtr
                nodePtr = nodePtr.next
                i += 1
                
            elif i == length//2:
                prev.next = nodePtr.next
                return head
                
            
# using fast and slow pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast,slow = head.next.next,head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head
