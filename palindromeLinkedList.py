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
        
# JavaScript Cleaner Code (https://leetcode.com/problems/palindrome-linked-list/discuss/1419886/95-faster-JS-solution-with-O(1)-space-complexity)
# var isPalindrome = function(head) {
#     //edage case
#     if (!head) return true;
    
#     //find the middle point use two point runner 
#     let slow = head;
#     let fast = head;
#     let wholeList = head;
#     while (fast.next && fast.next.next) {
#         slow = slow.next;
#         fast = fast.next.next;
#     }
#     //flip the second half
#     let secondHalf = reverseList(slow.next);
    
#     //compare with secondHalf with wholelist
#     while(secondHalf){
#         if (secondHalf.val !== wholeList.val) return false;
#         secondHalf = secondHalf.next;
#         wholeList = wholeList.next;
#     }
    
#     return true;
# };

# const reverseList = (head) => {
#     if (!head) return null;
    
#     let prev = null;
#     while (head) {
#       let temp = head.next;
#         head.next = prev;
#         prev = head;
#         head = temp;
#     }
    
#     return prev;
# }