from random import choice


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.array = []

    # O(1) Time
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.array)
        self.array.append(val)
        return True

    # O(1) Time
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val]
        last_elem = self.array[-1]

        self.array[idx] = last_elem
        self.map[last_elem] = idx

        self.array.pop()
        del self.map[val]
        return True

    # O(1) Time
    def getRandom(self) -> int:
        return choice(self.array)


if __name__ == '__main__':
    random_set = RandomizedSet()

    print(random_set.insert(1))
    print(random_set.remove(2))
    print(random_set.insert(2))
    print(random_set.getRandom())
    # print(random_set.getRandom())
