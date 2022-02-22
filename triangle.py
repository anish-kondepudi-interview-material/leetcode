class Solution:
    
    def helper(self, triangle, row, idx, memo):
        if row == len(triangle):
            return 0
        if (row,idx) in memo:
            return memo[(row,idx)]
        
        minPathSum = triangle[row][idx]+min(self.helper(triangle, row+1, idx, memo), 
                                            self.helper(triangle, row+1, idx+1, memo))
        
        memo[(row,idx)] = minPathSum
        return minPathSum
        
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.helper(triangle,0,0,{})
