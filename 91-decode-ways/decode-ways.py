class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        prev = 1  
        curr = 1 

        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp += curr
            
            if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                temp += prev
            
            prev, curr = curr, temp
        return curr