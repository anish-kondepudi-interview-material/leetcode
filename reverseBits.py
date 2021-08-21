class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(bin(n)[:1:-1])
        x += '0'*(32-len(x))
        return int(x,2)