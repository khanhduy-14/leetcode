class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = 0
        min_ending = 0
        res = 0
        for i in range(0, len(nums)):
            max_ending = max(max_ending + nums[i], 0)
            min_ending = min(min_ending + nums[i], 0)

            res = max(res, max_ending, -min_ending)

        return res
        