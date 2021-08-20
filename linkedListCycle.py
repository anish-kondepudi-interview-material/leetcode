# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(N) time, O(1) Space
    # Another solution is to invert pointer direction (this keeps values intact)
    # If Linked List must stay intact, use set(), O(N) space
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None or head.next is None:
            return False
        
        currNode = head
        while currNode:
            if currNode.val == 100001:
                return True
            currNode.val = 100001
            currNode = currNode.next
            
        return False
        
        