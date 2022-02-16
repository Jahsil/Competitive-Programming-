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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode nodePtr = head ;
        int length = 0;
        while(nodePtr != null){
            length += 1;
            nodePtr = nodePtr.next;
        }
        int deletionNode = length - n + 1;
        ListNode temp , prev ; 
        temp = head ; 
        prev = null ; 
        int i = 1;
        while(i < deletionNode){
            i ++ ; 
            prev = temp ; 
            temp = temp.next;
        }if(temp.next == head){
            return head.next;
        }
        prev.next = temp.next;
        return head;
    }
}
