from heapq import heappop, heappush, heapify

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        headNode = ListNode()
        currNode = headNode
        
        # Build Heap
        heap = []
        for uid, node in enumerate(lists):
            if node is None: continue
            heap.append((node.val,uid,node.next))
        heapify(heap)
        
        # Merge Linked Lists
        uid = len(heap)+1
        while len(heap) != 0:
            val, _, nextNode = heappop(heap)
            currNode.next = ListNode(val)
            currNode = currNode.next
            if nextNode is None: continue
            heappush(heap,(nextNode.val,uid,nextNode.next))
            uid += 1
        
        return headNode.next
                
                    
            
            
