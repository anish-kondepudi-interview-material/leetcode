from collections import deque
class Solution:
    
    def isMutation(self, s1, s2):
        duplicate = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                duplicate += 1
                if duplicate > 1: return False
        return True
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque()
        q.append((start,0))
        
        visited = set()
        
        while len(q) != 0:
            currGene, currDist = q.popleft()
            visited.add(currGene)
            if currGene == end: return currDist
            for gene in bank:
                if gene in visited: continue
                if self.isMutation(currGene,gene):
                    q.append((gene,currDist+1))
            
        return -1