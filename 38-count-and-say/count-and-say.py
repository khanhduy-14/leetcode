class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n <= 1:
            return str(n)
        
        say = '1'

        for i in range(1,n):
            say = self.countString(say)
        return say


    def countString(self, s: str) -> str:
        freq = 1
        result = ''
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                freq+=1
            else:
                result+= str(freq)
                result+=s[i-1]
                freq = 1
        result+= str(freq)
        result+=s[-1]
        return result