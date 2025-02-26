class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = nums[0]
        min_ending = nums[0]
        res = abs(nums[0])
        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])
            min_ending = min(min_ending + nums[i], nums[i])
            abs_max_ending = max(abs(max_ending), abs(min_ending))

            res = max(res, abs_max_ending)

        return res
        