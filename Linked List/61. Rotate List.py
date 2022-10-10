# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
        if not head:
            return None
        length = 0
        start = head
        while start:
            start = start.next
            length += 1
        if k == 0 or k % length == 0 or  not head.next:
            return head
        start = head 
        i = 0 
        while i < k % length:
            start = head
            end = head.next
            tmp = head
            while end.next:
                end = end.next
                start = start.next
            start.next = None
            end.next = tmp
            head = end 
            i += 1
            
        return end
