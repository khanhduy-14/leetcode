class Solution:
    def rob(self, nums: List[int]) -> int:
         prev_rob = 0
         profit = 0
         for num in nums:
            curr_rob = prev_rob + num
            prev_rob=profit
            profit = max(profit, curr_rob)
        
         return profit


        