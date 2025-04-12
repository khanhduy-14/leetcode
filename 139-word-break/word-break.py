class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        wordSet = set(wordDict)
        dp[0] = True

        for i in range(n):
            for word in wordDict:
                if dp[i] and s[i:i+len(word)] in wordSet and i + len(word) <= n:
                    dp[i+len(word)] = True

        return dp[-1]