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
    public void reorderList(ListNode head) {
        if (head.next == null) {
            return;
        }
        ListNode tort = head;
        ListNode hare = head;
        while (hare != null && hare.next != null) {
            tort = tort.next;
            hare = hare.next.next;
        }
        ListNode current = tort.next;
        tort.next = null;
        ListNode prev = tort;
        System.out.println(current.val);

        
        ListNode temp = current;
        while (current != null) {
            current = current.next;
            temp.next = prev;
            prev = temp;
            temp = current;
        }
        
        System.out.println(prev.val);
        ListNode tail = prev;
        temp = head;
        System.out.println(temp.val);
        int choice = 1;
        while (tail != head) {
            if (choice == 1) {
                temp = head.next;
                head.next = tail;
                head = temp;
                choice = 0;
            }
            else {
                temp = tail.next;
                tail.next = head;
                tail = temp;
                choice = 1;
            }

        }
    }
}
