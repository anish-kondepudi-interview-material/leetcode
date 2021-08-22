
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0: return False
        if n == 1: return True
        num = 3
        while num < n:
            num *= 3
        return n == num
               
        
        # https://leetcode.com/problems/power-of-three/solution/
        #
        # 1. Loop and continually divide by 3
        #
        # 2. Convert to base 3 and see if it's 1 followed by all 0s
        #
        # 3. Use Math, check if i = log(n)/log(3) is an integer (i.e. logn/log3 % 1 == 0)
        #