class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        normallySatisfied = 0
        for grump, customer in zip(grumpy, customers):
            normallySatisfied += int(not grump)*customer
            
        maxSatisfied = 0
        for grump, customer in zip(grumpy[:minutes], customers[:minutes]):
            maxSatisfied += grump*customer
        
        currSatisfied = maxSatisfied
        for i in range(1, len(customers)-minutes+1):
            currSatisfied += (grumpy[i+minutes-1]*customers[i+minutes-1]) - (grumpy[i-1]*customers[i-1])
            maxSatisfied = max(maxSatisfied, currSatisfied)
            
        return normallySatisfied+maxSatisfied
            
            
            
                
