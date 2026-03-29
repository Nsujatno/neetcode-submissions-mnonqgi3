class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we can do this by reversing the matrix vertically and then transposing it
        matrix.reverse()

        # transpose matrix by swapping elements across the diagonal
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]