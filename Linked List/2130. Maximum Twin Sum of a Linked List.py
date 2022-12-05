# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(head):
            curr = head
            prev = None
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
        
        length = 0
        curr = head
        # Finding the length
        while curr:
            length += 1
            curr = curr.next
        mid = length // 2 
        # Finding the midpoint
        curr = head
        for i in range(mid):
            curr = curr.next
        # Second half of the linked list
        newCurrent = reverse(curr)
        
        curr = head
        maxVal = 0
        while curr and newCurrent:
            sm = curr.val + newCurrent.val
            if  sm >= maxVal:
                maxVal = sm
            curr = curr.next
            newCurrent = newCurrent.next
                
        return maxVal
                
        
        
        
        
        
        
        
        
        
        
            
        
