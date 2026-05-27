# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry_in = 0

        while l1 or l2 or carry_in:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            summ = l1_val + l2_val + carry_in

            carry_in = summ // 10
            summ = summ % 10

            current.next = ListNode(summ)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next