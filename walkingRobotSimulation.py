class Solution:
    
    def getNewDirection(self, direction, turn):
        if turn == -2:
            return "NESW"["NESW".index(direction)-1]
        else:
            return "WSEN"["WSEN".index(direction)-1]
    
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = "N"
        x, y = 0, 0
        
        directionMapping = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }
        obstaclesSet = set([(x,y) for x,y in obstacles])
        
        maxDist = 0
        for command in commands:
            if command > 0:
                dx, dy = directionMapping[direction]
                while command:
                    if (x+dx, y+dy) in obstaclesSet: break
                    x += dx
                    y += dy
                    newDistSq = abs(x)**2 + abs(y)**2
                    maxDist = max(maxDist, newDistSq)
                    command -= 1
            else:
                direction = self.getNewDirection(direction, command)
                    
        return maxDist
                
        
