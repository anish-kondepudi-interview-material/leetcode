class Solution:     
    
    def climbStairs(self, n: int) -> int:
        
        def numWaysClimbStairs(n, memo):
            if n <= 1: return 1
            if memo[n] != -1:
                return memo[n]
            returnVal = numWaysClimbStairs(n-1,memo) + numWaysClimbStairs(n-2,memo)
            memo[n] = returnVal
            return returnVal
    
    
        memo = [-1]*(n+1)
        return numWaysClimbStairs(n, memo)



# BELOW ARE NOT MY SOLUTIONS (I LIKED THESE BOTTOM UP EXPLANATIONS, SO I AM KEEPING THEM HERE)

# use memorization to store, sacrifice space complexity
class Solution:
    def climbStairs(self, n: int) -> int:
        result = {1:1,2:2}
        for i in range(3,n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]
# This one only requires Time O(n) and Space O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return n
        one_step, two_step = 2,1   # these are the initial ways to get to stair 2 and stair 1
        current = 0
        for i in range(2,n):
            current = one_step + two_step  # either jump one step from the stair(n-1) or jump two from stair(n-2)
            # inplace renewal for next loop
            two_step = one_step    
            one_step = current    
            
        return current