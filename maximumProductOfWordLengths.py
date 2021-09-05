class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i, start_word in enumerate(words):
            word_set = set([x for x in start_word])
            word_len = len(start_word)
            for j, word in enumerate(words):
                if i == j: continue
                isDuplicate = False
                for c in word:
                    if c in word_set:
                        isDuplicate = True
                        break
                if not isDuplicate:
                    res = max(res,word_len*len(word))
        return res
    
    # More Efficient Bitwise Solution
    # https://www.youtube.com/watch?v=3XHAikDnB2w