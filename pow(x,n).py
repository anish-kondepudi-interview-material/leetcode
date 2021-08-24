from math import floor, ceil
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def findPow(x,n,memo):
            if n in memo.keys():
                return memo[n]
            memo[n] = findPow(x,floor(n/2),memo) * findPow(x,ceil(n/2), memo)
            return memo[n]
        
        memo = {0:1, 1:x}
        return findPow(x,abs(n),memo) if n > 0 else 1/findPow(x,abs(n),memo)