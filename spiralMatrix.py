class Solution:
    
    def isValid(self, matrix, i, j):
        return (i>=0 and i<len(matrix) and j>=0 and j<len(matrix[0]) and matrix[i][j]!=101)
    
    def isDone(self, matrix, i, j):
        if i+1<len(matrix) and matrix[i+1][j] != 101: return False
        if i-1>=0 and matrix[i-1][j] != 101: return False
        if j+1<len(matrix[0]) and matrix[i][j+1] != 101: return False
        if j-1>=0 and matrix[i][j-1] != 101: return False
        return True
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge Case
        if len(matrix) == 1 and len(matrix[0]) == 1: return matrix[0]
        
        directions = [ (0,1), (1,0), (0,-1), (-1,0) ]
        direction = 0
        
        res = []
        i = 0
        j = 0
        
        while True:
            # Get direction
            di, dj = directions[direction]
            
            # Check if new cell is valid (Cycle direction is needed)
            if not self.isValid(matrix,i+di,j+dj):
                direction = (direction+1) if direction!=3 else 0
                continue
            
            # Add cell to matrix and mark as seen
            res.append(matrix[i][j])
            matrix[i][j] = 101
            
            # Move to next cell
            i = i+di
            j = j+dj
            
            # If if no more potential movements, return
            if self.isDone(matrix,i,j):
                res.append(matrix[i][j])
                return res
            
    # Alternate solution is to update boundaries: https://leetcode.com/problems/spiral-matrix/solution/
            
            
            
            