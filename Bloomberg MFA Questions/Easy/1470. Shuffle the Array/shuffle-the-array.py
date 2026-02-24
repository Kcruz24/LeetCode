from typing import List

'''

- First, i'll get a pointer right in the middle of the list

[2, 5, 1, 3, 4, 7]
          |       |

[2, 3, 5, 4, 1, 7]
'''


class Solution:
    # O(N) Time | O(N) Space
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        interweaved_arr = []

        for x, y in zip(nums, nums[n:]):
            interweaved_arr.append(x)
            interweaved_arr.append(y)

        return interweaved_arr


if __name__ == '__main__':
    sol = Solution()

    nums = [2, 5, 1, 3, 4, 7]
    n = 3

    print(sol.shuffle(nums, n))
