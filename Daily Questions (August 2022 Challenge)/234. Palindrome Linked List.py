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
        
        
        
        # Using Two Pointers
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = head
        s = ""
        while start:
            s += str(start.val)
            start = start.next
        
        left , right = 0 , len(s) - 1   
        
        while(left < right):
            if (s[left] != s[right]):
                return False
            right -= 1
            left += 1
            
        return True
            
            
            
