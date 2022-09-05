class Bitset:
    # O(1) Time | O(N) Space
    def __init__(self, size):
        self.bitset = [0 for _ in range(size)]
        self.flipped = False
        self.size = size
        self.ones = 0

    # O(1) Time
    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bitset[idx] == 1:
                self.bitset[idx] = 0
                self.ones += 1
        else:
            if self.bitset[idx] == 0:
                self.bitset[idx] = 1
                self.ones += 1

    # O(1) Time
    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bitset[idx] == 0:
                self.ones -= 1
                self.bitset[idx] = 1
        else:
            if self.bitset[idx] == 1:
                self.bitset[idx] = 0
                self.ones -= 1

    # O(1) Time
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    # O(1) Time
    def all(self) -> None:
        return self.ones == self.size

    # O(1) Time
    def one(self) -> None:
        return self.ones > 0

    # O(1) Time
    def count(self) -> None:
        return self.ones

    # O(N) Time
    def toString(self) -> str:
        if self.flipped:
            return ''.join('0' if bit else '1' for bit in self.bitset)

        return ''.join([str(bit) for bit in self.bitset])


if __name__ == '__main__':
    bitset = Bitset(5)

    bitset.fix(3)
    print(bitset.toString())
    bitset.fix(1)
    print(bitset.toString())
    bitset.flip()
    print(bitset.toString())
    print(bitset.all())
    bitset.unfix(0)
    print(bitset.toString())
    bitset.flip()
    print(bitset.one())
    bitset.unfix(0)
    print(bitset.count())
    print(bitset.toString())
