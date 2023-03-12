from sortedcontainers import SortedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        sl = SortedList()

        for i in lists:
            curr = ListNode(float('-inf'))
            curr.next = i
            curr = curr.next
            while curr:
                sl.add(curr.val)
                curr = curr.next

        return self.arrayToList(sl , len(sl))
        
    def insert(self , root, item):
        temp = ListNode(item)
        
        if (root == None):
            root = temp
        else :
            ptr = root
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = temp
        
        return root

    def arrayToList(self , arr, n):
        root = None
        for i in range(0, n, 1):
            root = self.insert(root, arr[i])
        
        return root

        
            
