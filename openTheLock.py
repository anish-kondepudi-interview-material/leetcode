from collections import deque

class Solution:
    
    def getNeighbors(self, num, distance):
        neighbors = []
        
        for i in range(4):
            if(num[i]=='9'):
                neighbors.append(num[0:i]+'0'+num[i+1:])
                neighbors.append(num[0:i]+'8'+num[i+1:])
            elif(num[i]=='0'):
                neighbors.append(num[0:i]+'1'+num[i+1:])
                neighbors.append(num[0:i]+'9'+num[i+1:])
            else:
                neighbors.append(num[0:i]+str(int(num[i])+1)+num[i+1:])
                neighbors.append(num[0:i]+str(int(num[i])-1)+num[i+1:])
            
        return (neighbors,distance+1)
    
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = deque()
        q.append(("0000",0))
        
        seen = set()
        for deadend in deadends:
            seen.add(deadend)
            
        while len(q) != 0:
            num, distance = q.popleft()
            if num == target: return distance
            if num in seen: continue
            seen.add(num)
            neighbors, newDistance = self.getNeighbors(num, distance)
            for neighbor in neighbors:
                if neighbor in seen: continue
                q.append((neighbor,newDistance))
        
        return -1
        
        