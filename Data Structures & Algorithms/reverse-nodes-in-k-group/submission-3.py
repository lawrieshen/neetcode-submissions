# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(start):
            prev = None
            curr = start

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        dummy = ListNode()
        dummy.next = head
        prev_group_end = dummy

        while True:
            # find the start and the end of the group
            group_start = prev_group_end.next
            group_end = prev_group_end

            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next

            next_group_start = group_end.next

            group_end.next = None
            new_group_start = reverse_linked_list(group_start)

            prev_group_end.next = new_group_start
            group_start.next = next_group_start

            prev_group_end = group_start


