from heapq import heappush, heappop, heapify
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = defaultdict(int)
        for num in nums:
            occurrences[num] += 1
            
        heap = [(-v,k) for k,v in occurrences.items()]
        heapify(heap)
        
        kMostFreqEl = []
        for _ in range(k):
            kMostFreqEl.append(heappop(heap)[1])
            
        return kMostFreqEl

# O(N) Solution
# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         occurrences = defaultdict(int)
#         for num in nums:
#             occurrences[num] += 1

#         countArr = [[] for _ in range(len(nums)+1)]
#         for num,count in occurrences.items():
#             countArr[count].append(num)

#         topKFreqEl = []
#         for arr in reversed(countArr):
#             if k == 0: break
#             while len(arr) != 0:
#                 topKFreqEl.append(arr.pop())
#                 k -= 1

#         return topKFreqEl
