from heapq import heapify, heappop, heappush

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs) # Build Heap O(N)

        maxBars = 0
        while True:
            cheapestBar = heappop(costs)
            coins -= cheapestBar
            if coins < 0: break
            maxBars += 1
            if len(costs) == 0 or coins == 0: break

        return maxBars
