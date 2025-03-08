class Solution:
    def numSquares(self, n: int) -> int:
        dp = [2**32+1] * (n+1)
        dp[0]=0
        num = 1
        
        while num * num <= n:
            for i in range(num*num, n+1):
                dp[i] = min(dp[i-(num*num)] + 1, dp[i])
            num+=1
        


        return dp[n]
        