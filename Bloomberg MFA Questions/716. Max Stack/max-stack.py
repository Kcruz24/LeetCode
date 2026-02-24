'''

[5, 1, 5]

3
max_stack = [1, 3, 5, 7, 9, 11]
temp = [11, 9, 7, 5]


'''
import heapq


class MaxStack:

    def __init__(self):
        self.stack = []
        self.pq = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.pq, -x)

    def pop(self) -> int:
        elem = self.stack.pop()
        temp = []
        while self.pq[0] != elem:
            temp.append(-heapq.heappop(self.pq))

        heapq.heappop(self.pq)
        while temp:
            heapq.heappush(self.pq, temp.pop())

        return elem

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.pq[0]

    def popMax(self) -> int:
        elem = -heapq.heappop(self.pq)

        temp = []
        while elem != self.stack[-1]:
            temp.append(self.stack.pop())

        self.stack.pop()
        while temp:
            self.stack.append(temp.pop())

        return elem


class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.max_stack:
            if x >= self.max_stack[-1]:
                self.max_stack.append(x)
            else:
                temp = []
                top = self.max_stack[-1]
                while self.max_stack and x < top:
                    temp.append(self.max_stack.pop())
                self.max_stack.append(x)

                while temp:
                    self.max_stack.append(temp.pop())
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        elem = self.stack.pop()
        temp = []
        while self.max_stack[-1] != elem:
            temp.append(self.max_stack.pop())

        self.max_stack.pop()
        while temp:
            self.max_stack.append((temp.pop()))

        return elem

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        elem = self.max_stack.pop()
        temp = []
        while self.stack[-1] != elem:
            temp.append(self.stack.pop())

        self.stack.pop()
        while temp:
            self.stack.append((temp.pop()))

        return elem

        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()
