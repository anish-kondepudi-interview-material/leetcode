class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted([(a, b, b - a) for a, b in costs], key = lambda x: x[2], reverse = True)
        
        minCost = 0
        for i in range(len(costs)//2):
            minCost += costs[i][0] + costs[-i-1][1]
        return minCost
            
