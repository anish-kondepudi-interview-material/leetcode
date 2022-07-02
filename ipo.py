from heapq import heapify, heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        minHeap = [(c,p) for p,c in zip(profits,capital)]

        heapify(minHeap)

        while k > 0:
            while minHeap and minHeap[0][0] <= w:
                c, p = heappop(minHeap)
                heappush(maxHeap, -p)
            if maxHeap:
                p = -1 * heappop(maxHeap)
                w += p
                k -= 1
            else:
                break

        return w
            

