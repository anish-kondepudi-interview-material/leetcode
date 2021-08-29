class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        # Transpose
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Vertical Flip
        for i in range(N//2):
            for j in range(N):
                matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
            