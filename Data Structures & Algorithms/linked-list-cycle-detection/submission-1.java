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
    public boolean hasCycle(ListNode head) {
        ListNode hare = head;
        ListNode tort = head;
        if (head == null) {
            return false;
        }
        while (hare != null && tort != null) {
            hare = hare.next;
            if (hare == null) {
                return false;
            }
            else {
                hare = hare.next;
            }
            tort = tort.next;
            if (tort == hare) {
                return true;
            }
        }
        return false;
    }
}
