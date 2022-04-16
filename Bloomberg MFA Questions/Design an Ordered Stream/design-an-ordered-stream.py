from typing import List
from collections import deque


# O(N) time | O(N) space
class OrderedStream3:
    def __init__(self, n: int):
        self.stream = [None for _ in range(n)]
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id - 1] = value

        ordered_stream = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            ordered_stream.append(self.stream[self.ptr])
            self.ptr += 1

        return ordered_stream


class OrderedStream2:
    def __init__(self, n: int):
        self.seen = {}
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        seen, ptr = self.seen, self.ptr

        seen[id] = value
        result = []
        while ptr in seen:
            result.append(seen[ptr])
            del seen[ptr]
            ptr += 1

        self.ptr = ptr

        return result


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [[] for _ in range(n)]
        self.ptr = 0

    def insert(self, id_key: int, value: str) -> List[str]:

        if id_key - 1 != self.ptr:
            if value not in self.stream:
                self.stream[id_key - 1].append(value)

            return self.stream[self.ptr]

        if id_key - 1 == self.ptr:

            if value not in self.stream:
                self.stream[self.ptr].append(value)

            temp = self.ptr
            if temp < len(self.stream):
                while self.stream[temp + 1]:
                    pop_val = self.stream[temp + 1].pop()
                    self.stream[self.ptr].append(pop_val)
                temp += 1

            self.ptr += 1 if temp == 0 else temp

        print(self.ptr)

        return self.stream


if __name__ == "__main__":
    os = OrderedStream3(5)
    os.insert(3, "ccccc")
    os.insert(1, "aaaaa")
    os.insert(2, "bbbbb")
    os.insert(5, "eeeee")
    os.insert(4, "ddddd")
