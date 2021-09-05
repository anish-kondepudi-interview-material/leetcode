class Solution:
   
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalGas = 0
        currGas = 0
        
        startStation = 0
        
        for i in range(len(gas)):
            
            totalGas += gas[i]-cost[i]
            currGas += gas[i]-cost[i]
            
            if currGas < 0:
                startStation = i+1
                currGas = 0
        
        return startStation if totalGas>=0 else -1
        