"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # weave the original list and the cloned list together
        cur = head
        while cur:
            cloned = Node(cur.val)
            cloned.next = cur.next
            cur.next = cloned
            cur = cloned.next

        # adjust the random pointer
        cur = head
        while cur:
            cloned = cur.next
            cloned.random = cur.random.next if cur.random else None
            cur = cloned.next

        # break the weaved list
        original_list = head
        cloned_list = head.next
        new_head = head.next

        while original_list:
            original_list.next = cloned_list.next
            cloned_list.next = cloned_list.next.next if cloned_list.next else None
            original_list = original_list.next
            cloned_list = cloned_list.next
        
        return new_head