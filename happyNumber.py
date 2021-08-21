class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while n != 1:
            nStr = str(n)
            sum = 0
            for c in nStr:
                sum += int(c)**2
            n = sum
            if n in s:
                return False
            s.add(n)
        return True
        