class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dp[0] = min(dp[0] + cost[i] , dp[1] + cost[i])
            dp[0], dp[1] = dp[1], dp[0]

        return min(dp[0], dp[1])
        