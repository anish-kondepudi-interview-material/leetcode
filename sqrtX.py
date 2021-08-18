class Solution:
    # Binary Search O(logn)
    def mySqrt(self, x: int) -> int:
        
        if x <= 1: return x
    
        low = 0
        high = x
        
        while True:
            
            mid = (low+high)//2
            midSq = mid*mid
            
            if midSq == x:
                return mid
            
            if midSq > x:
                high = mid
            elif midSq < x:
                if (mid+1)*(mid+1) > x:
                    return mid
                low = mid
            
            