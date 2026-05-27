# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initiate an array as heap
        heap = []

        # add all nodes in to heap while sorting
        for i, _list in enumerate(lists):
            if _list:
                # need to handle edge case when _list.val is same, then we compare which list is the node in
                heapq.heappush(heap, (_list.val, i, _list))

        # connect all node in heap by order
        dummy = ListNode()
        current = dummy
        while heap:
            val, i, node  = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))


        return dummy.next