class Solution:
    def getNeighbors(self,board,i,j):
        neighbors = []
        if i > 0: neighbors.append((-1,0))
        if i < len(board)-1: neighbors.append((1,0))
        if j > 0: neighbors.append((0,-1))
        if j < len(board[0])-1: neighbors.append((0,1))
        return neighbors
        
    
    def dfs(self, board, word, i, j, visited):
        if (i,j) in visited: return False
        if board[i][j] == word: return True
        if board[i][j] != word[-1]: return False
        
        visited.add((i,j))
        word = word[:-1]
    
        for neighbor in self.getNeighbors(board,i,j):
            di,dj = neighbor
            if self.dfs(board,word,i+di,j+dj,visited):
                return True
        
        visited.remove((i,j))
        return False
                    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0: return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,i,j,set()):
                    return True
                
        return False