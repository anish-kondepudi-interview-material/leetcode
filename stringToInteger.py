class Solution:
    # Ugly solution (Hacky and Slow)
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = 0
        for i, char in enumerate(s):
            if char in {'0','1','2','3','4','5','6','7','8','9'}:
                start = i
                break
            elif char in ('-','+'):
                if i+1 == len(s):
                    return 0
                if s[i+ 1] not in {'0','1','2','3','4','5','6','7','8','9'}:
                    return 0
            elif char not in {' '}:
                return 0
        end = len(s)-1
        for i in range(start,len(s)):
            char = s[i]
            if char not in {'0','1','2','3','4','5','6','7','8','9'}:
                end = i-1
                break
                
        print(start,end)
                
        if end < start:
            return 0
        num = int(s[start:end+1])
        if start > 0:
            if s[start-1] == '-':
                num *= -1
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num
    
    # Better Solution (Fasater + Cleaner)
    # Doesn't take advantage of Pythons >32 Bit Integers
    # Accounts for overflow legit
    # https://leetcode.com/problems/string-to-integer-atoi/discuss/1419853/Python-or-28ms-(greater93.93)-14.5-MB-or-Overflow-secure-WO-regex
    # class Solution:
    # def myAtoi(self, s: str) -> int:
    #     number = 0
    #     found_valid_chars = False
    #     negative = None
    #     i = 0
    #     while i < len(s):
    #         c = s[i]
    #         if '0' <= c <= '9':
    #             found_valid_chars = True
    #             if not negative:
    #                 if number <= (2**31-1-int(c))/10:
    #                     number = number*10 + int(c)
    #                 else:
    #                     return 2**31-1
    #             else:
    #                 if number >= (-2**31+int(c))/10:
    #                     number = number *10 - int(c)
    #                 else:
    #                     return -2**31
    #         else:
    #             if found_valid_chars:
    #                 # Didn't recognized a number and already removed leading ' ' so break it
    #                 break
    #             elif c == '+':
    #                 negative = False
    #                 found_valid_chars = True
    #             elif c == '-':
    #                 negative = True
    #                 found_valid_chars = True
    #             elif c == ' ':
    #                 pass
    #             else:
    #                 break
    #         i+=1
    #     return number
    
            