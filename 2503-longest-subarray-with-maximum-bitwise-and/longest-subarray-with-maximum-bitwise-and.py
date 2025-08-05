class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num,len_curr_sub, res = max(nums), 0, 0

        for num in nums:
            if num == max_num:
                len_curr_sub+=1
                res = max(len_curr_sub, res)
            else:
                if len_curr_sub != 0:
                    len_curr_sub = 0
        return res


