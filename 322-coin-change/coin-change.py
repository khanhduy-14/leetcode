class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [2**32 - 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != 2**32 - 1 else -1
        