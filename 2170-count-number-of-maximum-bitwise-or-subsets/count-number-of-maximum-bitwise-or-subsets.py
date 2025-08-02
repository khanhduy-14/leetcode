class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or, dp = 0, {0: 1}
        for num in nums:
            max_or |= num
        
        for num in nums:
            for prev_or, cnt in list(dp.items()):
                curr_or = prev_or | num
                dp[curr_or] = dp.get(curr_or,0) + cnt
        
        return dp[max_or]