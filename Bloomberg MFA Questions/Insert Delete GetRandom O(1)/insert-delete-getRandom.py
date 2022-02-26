from random import choice


class RandomizedSet:

    def __init__(self):
        self.item_to_position = {}
        self.items = []

    # O(1) time | O(N) space
    def insert(self, val: int) -> bool:
        if val in self.item_to_position:
            return False

        self.items.append(val)
        self.item_to_position[val] = len(self.items) - 1
        return True

    # O(1) time | O(1) space
    def remove(self, val: int) -> bool:
        if val not in self.item_to_position:
            return False

        # [2]
        # 2: 0
        # position = 0
        # last_item = 2

        position = self.item_to_position.pop(val)
        last_item = self.items.pop()
        if position < len(self.items):
            self.items[position] = last_item
            self.item_to_position[last_item] = position
        return True

    # O(1) time | O(1) space
    def getRandom(self) -> int:
        return choice(self.items)


if __name__ == '__main__':
    random_set = RandomizedSet()


    # random_set.insert(1)
    # random_set.remove(2)
    # random_set.insert(2)
    # random_set.getRandom()
    # random_set.remove(1)
    # random_set.insert(2)
    # random_set.getRandom()

    random_set2 = RandomizedSet()

    random_set2.remove(0)
    random_set2.remove(0)
    random_set2.insert(0)
    random_set2.getRandom()
    random_set2.remove(0)
    random_set2.insert(0)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
