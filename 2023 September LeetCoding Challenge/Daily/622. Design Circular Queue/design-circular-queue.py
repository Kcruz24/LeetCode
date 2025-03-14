class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:
    # O(1) Time | O(k) Space
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head


    # O(1) Time
    def insert(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node

        self.tail.prev = node
        node.next = self.tail

        self.size += 1


    # O(1) Time
    def remove(self):
        node_to_remove = self.head.next
        self.head.next = node_to_remove.next
        node_to_remove.next.prev = self.head

        node_to_remove.next = None
        node_to_remove.prev = None

        self.size -= 1

    # O(1) Time
    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False

        new_node = Node(value)
        self.insert(new_node)

        return True

    # O(1) Time
    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.remove()

        return True

    # O(1) Time
    def Front(self) -> int:
        if self.head.next == self.tail:
            return -1

        return self.head.next.val

    # O(1) Time
    def Rear(self) -> int:
        if self.tail.prev == self.head:
            return -1

        return self.tail.prev.val

    # O(1) Time
    def isEmpty(self) -> bool:
        return self.size == 0

    # O(1) Time
    def isFull(self) -> bool:
        return self.size == self.max_size


if __name__ == '__main__':
    queue = MyCircularQueue(6)

    print(queue.enQueue(6))
    print(queue.Rear())
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.enQueue(5))
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.Front())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
