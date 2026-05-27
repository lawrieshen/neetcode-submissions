# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(start):
            prev = None
            current = start

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            return prev

        
        dummy = ListNode()
        dummy.next = head
        prev_group_end = dummy


        while True:
            # find the start and end of the group
            group_start = prev_group_end.next
            group_end = prev_group_end

            # traverse to the end of the group
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next # If there no enough nodes left, terminate everything

            next_group_start = group_end.next
            
            group_end.next = None
            new_group_start = reverse_linked_list(group_start)            

            # reconnection
            prev_group_end.next = new_group_start
            group_start.next = next_group_start

            # update prev_group_end
            prev_group_end = group_start