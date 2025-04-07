class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = ''
        for i in range(0,len(s)):
            for j in range(0, len(s) - i):
                if i == 0:
                    dp[j][j] = 1
                else:
                    if s[j] == s[j+i] and (i == 1 or dp[j+1][j+i-1] == 1):
                        dp[j][j+i] = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] and (j-i+1) > len(res):
                    res = s[i:j+1]

        return res

    

