class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def removeNode(self, node, delete):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        if delete: del node
        
    def insertAtHead(self, node):
        secondNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = secondNode
        secondNode.prev = node
        
    def deleteLRU(self):
        """
        Removes last Item in Linked List (LRU Item)
        Removes LRU item from Dictionary
        """
        deletedNode = self.tail.prev
        lastNode = self.tail.prev.prev
        lastNode.next = self.tail
        self.tail.prev = lastNode
        self.cache.pop(deletedNode.key, None)
        del deletedNode

    def get(self, key: int) -> int:
        """
        Moves Item to Front of Linked List
        Returns Item's Value
        """
        if key not in self.cache: return -1
        node = self.cache[key]
        self.removeNode(node,False)
        self.insertAtHead(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        """
        Removes LRU Item From LRU Cache if capacity is exceeded
        Inserts New Item into LRU Cache
        """
        if key in self.cache:
            self.removeNode(self.cache[key],True)
        elif len(self.cache) == self.capacity:
            self.deleteLRU()
        node = Node(key,value)
        self.cache[key] = node
        self.insertAtHead(node)

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
