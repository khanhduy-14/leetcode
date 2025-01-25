class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n <= 1:
            return str(n)
        
        say = '1'

        for i in range(1,n):
            groupCount = self.groupIdentical(say)
            say = ''.join(str(num) + char for num, char in groupCount)
        return say


    def groupIdentical(self, s: str) -> list[list[str]]:
        freq = 1
        groupCount = []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                freq+=1
            else:
                groupCount.append([freq, s[i - 1]])
                freq = 1
        groupCount.append([freq, s[-1]])
        return groupCount