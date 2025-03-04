class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sw = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        if s in sw:
            return True
        for i in range(len(s)):
            if dp[i]:
                for j in range(1, min(len(s) - i + 1, 20)):
                    print(s[i: i+j])
                    if s[i: i+j] in sw:
                        print(i+j)
                        dp[i + j]=True
        return dp[len(s)]
        