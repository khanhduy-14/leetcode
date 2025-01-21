class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = { "i": 0, "j": 0}
        db = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            db[i][i] = True
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                db[i][i+1] = True
                ans['i'] = i
                ans['j'] = i + 1
        
        for diff in range(2, len(s)):
            for i in range(0, len(s) - diff):
                j = i + diff
                if s[i] == s[j] and db[i+1][j-1]:
                        db[i][j] = True
                        ans['i'] = i
                        ans['j'] = j
            
        
        return s[ans['i']:ans['j'] + 1]

    

