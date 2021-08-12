class Solution:
    # O(n)
    def romanToInt(self, s: str) -> int:
        
        convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X' : 10, 'V': 5, 'I': 1}
        
        prevChar = 'I'
        answer = 0
        
        for char in s[::-1]:
            
            if convert[char] >= convert[prevChar]:
                answer += convert[char]
                prevChar = char
            else:
                answer -= convert[char]
                
        return answer
    
        # Can change to while loop to remove reversing the string O(2n) -> O(n)
            