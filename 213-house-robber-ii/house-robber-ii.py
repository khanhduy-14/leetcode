class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if len(nums)==1:
            return nums[0]
        def max_profit(start,end):
            prev, profit = 0,0
            for i in range(start, end):
               
                curr_profit = prev + nums[i]
                prev = profit
                profit = max(curr_profit, profit)
            return profit
        return max(max_profit(0,len(nums)-1), max_profit(1, len(nums)))
        