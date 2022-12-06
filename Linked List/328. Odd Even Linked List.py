# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next and head.next.next:
            slow = head
            fast = head
            nodePtr = slow
            nodePtrFast = fast.next
            while slow and fast and fast.next and fast.next.next :
                fast = slow.next
                tmp = fast.next
                slow.next = tmp
                fast.next = tmp.next
                slow = tmp

            slow.next = nodePtrFast      
            return nodePtr
        else:
            return head


