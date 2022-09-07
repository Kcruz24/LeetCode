from typing import List


class Solution:
    # O(M * N) time | O(1) space
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_length = len(matrix)
        col_length = len(matrix[0])
        up = 0
        left = 0
        right = col_length - 1
        down = row_length - 1

        order = []
        while len(order) < row_length * col_length:
            # Left to right
            for col in range(left, right + 1):
                order.append(matrix[up][col])

            # Traverse downwards
            for row in range(up + 1, down + 1):
                order.append(matrix[row][right])

            # Make sure we are not on the same row
            if up != down:
                # Traverse from right to left
                for col in range(right - 1, left - 1, -1):
                    order.append(matrix[down][col])

            # Make sure we are not on the same column
            if left != right:
                # Traverse upwards
                for row in range(down - 1, up, -1):
                    order.append(matrix[row][left])

            up += 1
            right -= 1
            down -= 1
            left += 1

        return order


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    sol = Solution()

    print(sol.spiralOrder(matrix))
