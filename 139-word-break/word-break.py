class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        wordSet = set(wordDict)
        dp[0] = True

        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True

        return dp[-1]