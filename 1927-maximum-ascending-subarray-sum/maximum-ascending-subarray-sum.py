class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = curr_sum + nums[i] if nums[i] > nums[i-1] else nums[i]
            if curr_sum >= max_sum:
                max_sum = curr_sum
        return max_sum