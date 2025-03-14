from typing import List


class Solution:
    # O(N) Time | O(1) Space
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n // 2 + n % 2):
            for col in range(n // 2):
                temp = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - col - 1]
                matrix[n - 1 - row][n - col - 1] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = matrix[row][col]
                matrix[row][col] = temp



class Solution:
    # O(N) Time | O(1) Space
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    def reflect(self, matrix):
        n = len(matrix)
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][-col -
                                              1] = matrix[row][-col - 1], matrix[row][col]
