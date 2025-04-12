class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        

        n = len(nums)
        target = s // 2
        dp = [True] + [False] * s
        for i in range(n):
           

            for j in range(s, -1, -1):
                if dp[j]:
                    dp[j + nums[i]] = True
        return dp[target]