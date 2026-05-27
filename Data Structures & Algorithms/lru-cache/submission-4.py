class Node:

    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node):
        # add to the front
        original_node = self.head.next

        self.head.next = node
        original_node.prev = node

        node.next = original_node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)

            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)

        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.prev.key)
            self._remove(self.tail.prev)