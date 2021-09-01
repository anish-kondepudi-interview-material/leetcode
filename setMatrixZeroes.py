class Solution:
    
    def setZeroRow(self, matrix, row):
        for col in range(len(matrix[row])):
            matrix[row][col] = 0
            
    def setZeroCol(self, matrix, col):
        for row in range(len(matrix)):
            matrix[row][col] = 0
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seenRows = set()
        seenCols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seenRows.add(i)
                    seenCols.add(j)
        
        for row in seenRows:
            self.setZeroRow(matrix,row)
        for col in seenCols:
            self.setZeroCol(matrix,col)
            
        # Constant Space Solution Below
        # Make 1st of each row/col a 0 if you want entire row/col to be 0
        # https://leetcode.com/problems/set-matrix-zeroes/solution/
        