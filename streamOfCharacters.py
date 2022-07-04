from collections import defaultdict, deque

class Node:
    def __init__(self):
        self.char = "$"
        self.children = defaultdict(lambda: Node())

class StreamChecker:
        
    def _insertWordIntoTrie(self, root, word):
        currNode = root
        for char in word:
            currNode = currNode.children[char]
            currNode.char = char
        currNode.children["$"]
    
    def __init__(self, words: List[str]):
        self.nodes = deque()
        self.root = Node()
        for word in words:
            self._insertWordIntoTrie(self.root, word)

    def query(self, letter: str) -> bool:
        matchFound = False
        nodesLen = len(self.nodes)
        
        for _ in range(nodesLen):
            currNode = self.nodes.popleft()
            if letter in currNode.children:
                newNode = currNode.children[letter]
                self.nodes.append(newNode)
                if "$" in newNode.children:
                    matchFound = True
                    
        if letter in self.root.children:
            newNode = self.root.children[letter]
            self.nodes.append(newNode)
            if "$" in newNode.children:
                matchFound = True
                
        return matchFound
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
