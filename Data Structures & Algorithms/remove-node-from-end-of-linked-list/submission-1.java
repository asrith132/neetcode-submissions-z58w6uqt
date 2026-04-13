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
        if (head.next == null) {
            return null;
        }
        ListNode current = head;
        ListNode prev = null;
        ListNode temp;
        while (current != null) {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        head = prev;
        ListNode tail = prev;
        prev = null;
        while (n > 1) {
            prev = tail;
            tail = tail.next;
            n--;
        }
        if (prev == null) {
            current = tail.next;
        }
        else {
            prev.next = tail.next;
            current = head;
        }

        prev = null;
        while (current != null) {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        head = prev;

        return head;

    }
}
