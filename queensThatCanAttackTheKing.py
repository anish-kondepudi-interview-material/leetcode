class Solution:
    
    def countQueens(self, king, queens, di, dj):
        i, j = king
        while i < 8 and j < 8 and j >=0 and i >= 0:
            if (i,j) in queens:
                return [i,j]
            i += di
            j += dj
        return False
            
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        # Creating Queens Set
        queensSet = set()
        for i, j in queens:
            queensSet.add((i,j))
        
        # Checking all 8 directions for queens
        ans = []
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for i, j in directions:
            if x:=self.countQueens(king,queensSet,i,j):
                ans.append(x)
        
        return ans
        
        
        
        