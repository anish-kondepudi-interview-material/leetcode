class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        answer = ''
        
        a = a[::-1]
        b = b[::-1]
        
        remainder = 0
        
        i = 0
        while i < max(len(a),len(b)):
            
            x = 0
            y = 0
            
            if i < len(a): x = int(a[i])
            if i < len(b): y = int(b[i])
                
            sum = x + y + remainder
            
            if sum == 0:
                answer += '0'
                remainder = 0
            if sum == 1:
                answer += '1'
                remainder = 0
            if sum == 2:
                answer += '0'
                remainder = 1
            if sum == 3:
                answer += '1'
                remainder = 1            
            
            i += 1
            
        if remainder == 1:
            answer += '1'
        
        return answer[::-1]
            
        
        
        