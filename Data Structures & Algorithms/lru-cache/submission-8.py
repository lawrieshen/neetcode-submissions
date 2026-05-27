class ListNode:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookUp = {}

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insertFront(self, node: ListNode):
        next_node = self.head.next
        self.head.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.lookUp:
            return -1

        node = self.lookUp[key]
        self._remove(node)
        self._insertFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookUp:
            node = self.lookUp[key]
            self._remove(node)
        
        node = ListNode(key, value)
        self._insertFront(node)
        self.lookUp[key] = node

        if len(self.lookUp) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            self.lookUp.pop(node.key)