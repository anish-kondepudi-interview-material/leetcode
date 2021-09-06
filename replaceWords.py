class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isDone = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            # Adds word to trie
            def addWord(self, word):
                currNode = self.root
                
                for char in word:
                    if char not in currNode.children:
                        currNode.children[char] = TrieNode()
                    currNode = currNode.children[char]
                
                currNode.isDone = True
                
            # Checks to see if word exists in trie and returns it
            def checkWord(self, word):
                currNode = self.root
                currWord = ''
                
                for char in word:
                    
                    if char in currNode.children:
                        currWord += str(char)
                        currNode = currNode.children[char]
                    else:
                        return (False,currWord)
                    
                    if currNode.isDone:
                        return (True,currWord)
                    
                return (False,currWord)
            
        # Create trie
        trie = Trie()
        
        # Add words to trie
        for word in dictionary:
            trie.addWord(word)
        
        # Modify words that exist in trie
        res = ''
        for word in sentence.split():
            wordExists, trieWord = trie.checkWord(word)
            if wordExists:
                res += trieWord
            else:
                res += word
            res += ' '
            
        # Return Result
        return res[:-1]