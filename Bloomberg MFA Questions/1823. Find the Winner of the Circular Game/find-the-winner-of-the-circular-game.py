

'''

n = 5, k = 2
[1, 2, 3, 4, 5]
[1, 3, 4, 5]
[1, 3, 5]
[3, 5]
[3]

'''


class Solution:
    # O(N^2) Time | O(N) Space
    def findTheWinner(self, n: int, k: int) -> int:

        arr = [i for i in range(1, n + 1)]
        idx_to_pop = 0

        while len(arr) > 1:
            idx_to_pop = (idx_to_pop + k - 1) % len(arr)
            arr.pop(idx_to_pop)

        return arr[0]


class Solution:
    # O(N) Time | O(1) Space
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        Recursion formula: f(n) = (f(n - 1) + k) % n, f(n) = n, if f(n) == 0
        '''

        #base case: if n is 1, 1st person is the winner
        res = 1

        for i in range(2, n + 1):

            #Remove the next kth person from current winner
            res = (res + k) % i

            if res == 0:
                #ith person is the winner
                res = i

        return res

if __name__ == '__main__':
    n = 5
    k = 2

    sol = Solution()

    print(sol.findTheWinner(n, k))
