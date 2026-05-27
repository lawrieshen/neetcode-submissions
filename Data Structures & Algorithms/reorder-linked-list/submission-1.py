# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow  = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break the list
        prev, curr = None, slow.next
        slow.next = None

        # reverse the second half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # weave
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2  