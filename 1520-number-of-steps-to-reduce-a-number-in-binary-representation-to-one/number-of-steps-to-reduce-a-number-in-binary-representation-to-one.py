class Solution:
    def numSteps(self, s: str) -> int:
        
        n = len(s)
        carry = 0
        res = 0
        for i in range(n - 1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                res+=2
            else:
                res+=1
        return res + carry