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

        # weave original list and copied list tgt
        pointer = head
        while pointer:
            cloned = Node(pointer.val)
            cloned.next = pointer.next
            pointer.next = cloned
            pointer = cloned.next
        
        # adjust the random pointer
        pointer = head
        while pointer:
            cloned = pointer.next
            # pointer.random is the original node, pointer.radom.next is the cloned node
            cloned.random = pointer.random.next if pointer.random else None
            pointer = cloned.next

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