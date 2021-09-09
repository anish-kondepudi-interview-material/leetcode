import re
class Solution:
    
    def convertToArr(self, s):
        res = []
        start, end = 0, 0
        while start != len(s)+1:
            while end != len(s) and s[end].isdigit():
                end += 1
            res.append(s[start:end])
            if end != len(s): res.append(s[end])
            start = end+1
            end = start
        return res
    
    def pass1(self, arr):
        for i, val in enumerate(arr):
            if val == '*':
                arr[i+1] = str(int(arr[i-1])*int(arr[i+1]))
                arr[i] = '0'
                arr[i-1] = '0'
            elif val == '/':
                arr[i+1] = str(int(int(arr[i-1])/int(arr[i+1])))
                arr[i] = '0'
                arr[i-1] = '0'
                
    def pass2(self, arr):
        res = 0
        add = True
        for val in arr:
            if val == '+':
                add = True
            elif val == '-':
                add = False
            else:
                if add:
                    res += int(val)
                else:
                    res -= int(val)
        return res
    
    def calculate(self, s: str) -> int:
        s = re.sub(r"\s+", "", s, flags=re.UNICODE)
        arr = self.convertToArr(s.strip())
        self.pass1(arr)
        return self.pass2(arr)