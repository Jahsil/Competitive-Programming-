/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
         if(head == null){
            return null;
        }
        ListNode nodePtr = head;
        ListNode nextPtr = nodePtr.next;
       
        while(nextPtr != null){
            if(nodePtr.val != nextPtr.val){
                nextPtr = nextPtr.next;
                nodePtr = nodePtr.next;
            }else if(nodePtr.val == nextPtr.val){
                nextPtr = nextPtr.next;
                nodePtr.next = nextPtr;
            }
        }
        return head;
    }
}
