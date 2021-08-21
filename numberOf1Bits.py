class Solution:
    def hammingWeight(self, n: int) -> int:
        binStr = str(bin(n))
        return binStr.count('1')
        