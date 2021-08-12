class Solution:
    def reverse(self, x: int) -> int:
        reverse = int(str(x)[::-1]) if x>=0 else int('-'+str(x)[1:][::-1])
        return 0 if (reverse > 2**31 -1 or reverse < -2**31) else reverse