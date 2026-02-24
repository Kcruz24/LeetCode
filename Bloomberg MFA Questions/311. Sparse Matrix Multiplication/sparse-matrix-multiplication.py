from typing import List

'''
[[1,0,0],
 [-1,0,3]]

[[7,0,0],
 [0,0,0],
 [0,0,1]]

 [
     [0, 0, 0]
     [0, 0, 0]
 ]

   mat1 = [
       [1, -5]
    ]

    mat2 = [
        [12],
        [-1]
    ]
1 * 12 + -5 * -1
12 + 5 = 17
'''


class Solution:
    # Just Iterate
    # O(N*K*M) Time | O(1) Space
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        output = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row, row_elements in enumerate(mat1):
            for elem_idx, row_elem in enumerate(row_elements):

                for col, col_elem in enumerate(mat2[elem_idx]):
                    output[row][col] += row_elem * col_elem

        return output


class Solution:
    # List of lists
    # O(M*K*N) Time | O(M*K + K*N) Space
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix

        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        # Store the non-zero values of each matrix.
        A = compress_matrix(mat1)
        B = compress_matrix(mat2)

        ans = [[0] * n for _ in range(m)]

        for mat1_row in range(m):
            # Iterate on all current 'row' non-zero elements of mat1.
            for element1, mat1_col in A[mat1_row]:
                # Multiply and add all non-zero elements of mat2
                # where the row is equal to col of current element of mat1.
                for element2, mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col] += element1 * element2

        return ans


if __name__ == '__main__':
    mat1 = [[1, 0, 0], [-1, 0, 3]]
    mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().multiply(mat1, mat2))

    mat1 = [[1, -5]]
    mat2 = [[12],
            [-1]]

    print(Solution().multiply(mat1, mat2))
