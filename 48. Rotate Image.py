class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix