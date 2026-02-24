from collections import OrderedDict


# O(1) Time | O(C) Space - where "C" is the capacity
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    # O(1) Time
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    # O(1) Time
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Solution with Doubly Linked List
class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node

        self.tail.prev = node
        node.prev = prev_tail
        node.next = self.tail

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = None
        node.prev = None

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
