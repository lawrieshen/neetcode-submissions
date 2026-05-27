class ListNode:

    def __init__(self, key: int = -1, val: int = -1, next: ListNode = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur= cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)