class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = 0
        for i in range(0,len(s)):
            for j in range(0, len(s) - i):
                if i == 0:
                    dp[j][j] = 1
                    res+=1
                else:
                    if s[j] == s[j+i] and (i == 1 or dp[j+1][j+i-1] == 1):
                        dp[j][j+i] = 1
                        res+=1

        return res