# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listLen = 0
        
        currNode = head
        while currNode:
            listLen += 1
            currNode = currNode.next
        
        middleIdx = listLen//2
        
        if listLen == 2:
            return head.val == head.next.val
        
        currIdx = 1
        prevNode = head
        currNode = head.next
        startReverse = True
        while currNode:
            if currIdx > middleIdx:
                if startReverse:
                    prevNode.next = None
                    startReverse = False
                temp = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = temp
                currIdx += 1
            else:
                prevNode = currNode
                currNode = currNode.next
                currIdx += 1
        tail = prevNode

        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
            
        return True
        
        