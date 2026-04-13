# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        carry = 0
        prev = None
        while l1 or l2 or carry > 0:
            val_one = 0
            val_two = 0
            if l1 != None:
                val_one = l1.val
                l1 = l1.next
            if l2 != None:
                val_two = l2.val
                l2 = l2.next
            total = val_one + val_two + carry
            add = total % 10
            carry = total // 10

            curr.val = add
            if prev:
                prev.next = curr
            prev = curr
            curr = ListNode()
        
        return head

            
            
            



        