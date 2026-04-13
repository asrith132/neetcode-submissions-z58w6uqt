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
        int current_value = head.val;
        while (head != null) {
            if (current_value > head.val) {
                return true;
            } else {
                current_value = head.val;
            }
            head = head.next;
        }
        return false;
    }
}
