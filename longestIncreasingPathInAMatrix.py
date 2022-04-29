class Solution:
    
    def inBounds(self, matrix, i, j):
        return 0<=i<len(matrix) and 0<=j<len(matrix[0])
    
    def dfs(self, matrix, i, j, visited, memo):
        # print(matrix[i][j], i, j, visited)
        if (i,j) in memo:
            return memo[(i,j)]
        steps = 1
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for di, dj in dirs:
            ni, nj = i+di, j+dj
            if not self.inBounds(matrix, ni, nj): continue
            if (ni,nj) in visited: continue
            if matrix[i][j] <= matrix[ni][nj]: continue
            visitedCopy = visited.copy()
            visitedCopy.add((ni,nj))
            steps = max(steps, self.dfs(matrix, ni, nj, visitedCopy, memo)+1)
        memo[(i,j)] = steps
        return steps
            
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxSteps = 0
        memo = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s = set()
                s.add((i,j))
                maxSteps = max(maxSteps, self.dfs(matrix, i, j, s, memo))
        return maxSteps
