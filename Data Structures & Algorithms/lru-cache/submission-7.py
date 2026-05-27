class Node:
    def __init__(self, prev=None, next=None, key=-1, val=-1):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookUp = {} # {key: Node}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insertFront(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        result = -1
        if key in self.lookUp:
            node = self.lookUp[key]
            result = node.val
            self._remove(node)
            self._insertFront(node)
        
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.lookUp:
            old_node = self.lookUp[key]
            self._remove(old_node)

        new_node = Node(key=key, val=value)
        self._insertFront(new_node)
        self.lookUp[key] = new_node

        if len(self.lookUp) > self.capacity:
            del_node = self.tail.prev
            self._remove(del_node)
            self.lookUp.pop(del_node.key)