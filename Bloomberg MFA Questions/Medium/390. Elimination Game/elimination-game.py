'''
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


[2, 3, 4, 5, 6, 7, 8, 9]


arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]


Steps:
    1. Traverse through the input array by 2 steps and popping every element
    2. Do step 1 in reverse
    3. when the input array has 1 number left, we return that number

'''


class Solution:
    # O(N) Time | O(1) Space
    def lastRemaining(self, n: int) -> int:
        copy_arr = n
        while len(n) > 1:
            for i in range(0, len(copy_arr), 2):
                elem = arr[i]
                n.pop(i)

            for i in range(len(copy_arr) - 1, -1, -2):
                elem = arr[i]
                n.pop(i)

            copy_arr = n.copy()

        last_number = n[0]
        return last_number


class Solution2:
    # O(log(N)) Time | O(1) space
    def lastRemaining(self, n: int) -> int:
        first = 1
        distance = 1
        step = 0

        while n > 1:
            if step % 2 == 0 or n % 2 != 0:
                first += distance

            distance *= 2
            step += 1
            n = n // 2

        return first


if __name__ == '__main__':
    sol = Solution2()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(sol.lastRemaining(9))
