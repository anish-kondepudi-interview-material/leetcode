class Solution:
    
    def findDiag(self, mat, row, isRow):
        diag = []
        if isRow:
            i,j = row,0
        else:
            i,j=len(mat)-1,row
        while i >= 0 and j < len(mat[0]):
            diag.append(mat[i][j])
            i -= 1
            j += 1
        return diag
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = []
        
        for row in range(len(mat)):
            diags.append(self.findDiag(mat,row,True))
        for col in range(1,len(mat[0])):
            diags.append(self.findDiag(mat,col,False))
            
        res = []
        for i, diag in enumerate(diags):
            if i%2 == 0:
                res += diag
            else:
                res += diag[::-1]
                
        return res
        
