class Solution:
    # Sieve of Eratosthenes Algorithm
    # Time: O(n*log(log n))
    # Space: O(n)
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primesArr = [True]*(n+1)
        i = 2
        while i*i <= n+1:
            if primesArr[i]:
                j = i*i
                while j <= n:
                    primesArr[j] = False
                    j += i
            i += 1
        for x, y in enumerate(primesArr):
            if y:
                print(f'{x} ', end='')
        if primesArr[-1]:
            return primesArr.count(True)-3
        return primesArr.count(True) - 2