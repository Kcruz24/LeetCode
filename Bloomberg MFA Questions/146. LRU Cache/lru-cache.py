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
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# O(1) Time | O(C) Space - Where "C" is the capacity of the cache.


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = dict()
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # O(1) Time
    def add_node(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = node

        self.tail.prev = node
        node.prev = tail_prev
        node.next = self.tail

    # O(1) Time
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # O(1) Time

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add_node(node)

            return node.val

        return -1

    # O(1) Time
    def put(self, key, value):
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key, value)
        self.add_node(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            head_next = self.head.next
            self.remove(head_next)

            del self.map[head_next.key]
