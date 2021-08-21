class Solution:
    # Uses math for solution (count factors of 5 and 2
    # ignore 2 since factors of 5 > factors of 2
    def trailingZeroes(self, n: int) -> int:
        
        # Optimized for question constraints
        return n//5 + n//25 + n//125 + n//625 + n//3125
        
        # Works for all cases
        # if n == 0: return 0
        # zeros = 0
        # prevZeros = -1
        # divisor = 5
        # while prevZeros != zeros:
        #     prevZeros = zeros
        #     zeros += n//divisor
        #     divisor *= 5
        # return zeros
            
        