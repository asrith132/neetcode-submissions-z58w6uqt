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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return head;
        }
        ListNode current = head;
        ListNode next = current.next;
        ListNode dNext = next.next;
        current.next = null;
        while (dNext != null) {
            next.next = current;
            current = next;
            next = dNext;
            dNext = dNext.next;
        }
        next.next = current;
        return next;
    }
}
