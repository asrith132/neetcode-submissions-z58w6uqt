# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if curr1 == None:
            return list2
        if curr2 == None:
            return list1
        curr1_val = curr1.val
        curr2_val = curr2.val
        if curr1_val < curr2_val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        curr = head
        while curr1 != None and curr2 != None:
            curr1_val = curr1.val
            curr2_val = curr2.val
            if curr1_val < curr2_val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next
        if curr1 != None:
            curr.next = curr1
        elif curr2 != None:
            curr.next = curr2
        return head

                