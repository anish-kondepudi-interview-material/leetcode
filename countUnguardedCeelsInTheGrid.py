class Solution:
    
    def inBounds(self, i, j, m, n):
        return (0 <= i < m) and (0 <= j < n)
    
    def dfs(self, i, j, m, n, visited, guards, walls):
        
        visited.add((i,j))
        
        xi = i+1
        while self.inBounds(xi, j, m, n) and (xi, j) not in guards and (xi, j) not in walls:
            visited.add((xi, j))
            xi += 1
        
        xi = i-1
        while self.inBounds(xi, j, m, n) and (xi, j) not in guards and (xi, j) not in walls:
            visited.add((xi, j))
            xi -= 1
            
        xj = j+1
        while self.inBounds(i, xj, m, n) and (i, xj) not in guards and (i, xj) not in walls:
            visited.add((i, xj))
            xj += 1
            
        xj = j-1
        while self.inBounds(i, xj, m, n) and (i, xj) not in guards and (i, xj) not in walls:
            visited.add((i, xj))
            xj -= 1
        
        
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guardsSet = set([(i, j) for i, j in guards])
        wallsSet = set([(i, j) for i, j in walls])
        
        visited = wallsSet.copy()
        for i, j in guards:
            self.dfs(i, j, m, n, visited, guardsSet, wallsSet)
        
        return m*n - len(visited)
        
