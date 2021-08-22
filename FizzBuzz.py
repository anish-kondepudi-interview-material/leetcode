class Solution:
    
    def getString(self, n, a, b):
        answer = ''
        if n%a==0: answer += 'Fizz'
        if n%b==0: answer += 'Buzz'
        if n%a!=0 and n%b!=0: answer = str(n)
        return answer
    
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            result.append(self.getString(i,3,5))
        return result