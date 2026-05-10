class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(0, j):
                if dp[i] == -1:
                    continue
                diff = abs(nums[j] - nums[i])
          
                if diff <= target:
                    dp[j] = max(dp[i] + 1, dp[j])
        print(" ".join(map(str, dp)))
        return dp[n-1]