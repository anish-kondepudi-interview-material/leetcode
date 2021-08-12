class Solution:
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        reverseNum = 0
        
        isPositive = True if x >= 0 else False

        if not isPositive:
            x *= -1
            reverseNum = (x%10) * -1
            x //= 10

        while x != 0:
            if reverseNum > INT_MAX//10 or reverseNum < INT_MIN/10:
                return 0
            reverseNum = (reverseNum*10 + x%10) if isPositive else (reverseNum*10 - x%10)
            x //= 10
        
        return reverseNum