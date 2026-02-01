class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        sorted_nums = sorted(nums[1: n])
        return res + sorted_nums[0] + sorted_nums[1]