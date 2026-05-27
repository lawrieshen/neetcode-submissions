class Node:

    def __init__(self, key: int, value: int):
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
        self.tail.prev =  self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node):
        # always add to the frontmost position
        original_node = self.head.next
        
        self.head.next = node
        original_node.prev = node
        
        node.next = original_node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # find the old node
            node = self.cache[key]
            # remove the old node
            self._remove(node)
            # add node to the front of the list
            self._add(node)

            return node.value
        # if not found return -1
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # find old_node
            node_to_be_removed = self.cache[key]
            # remove old_node from linked list
            self._remove(node_to_be_removed)

        # create new node
        node = Node(key=key, value=value)

        # update new node to the cache
        self.cache[key] = node

        # add new node to the frontmost of the linked list
        self._add(node)

        # if exceed capacity
        if len(self.cache) > self.capacity:
            # remove LRU from stack
            self.cache.pop(self.tail.prev.key)
            # remove LRU from linked list
            self._remove(self.tail.prev)
            
