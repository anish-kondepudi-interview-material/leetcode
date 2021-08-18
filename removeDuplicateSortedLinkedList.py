# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return
        if head.next == None:
            return head
        
        startNode = head
        prevNode = head
        head = head.next
        
        while head:
            if head.val == prevNode.val:
                prevNode.next = head.next
                head = head.next
            else:
                prevNode = head
                head = head.next
        
        return startNode
        