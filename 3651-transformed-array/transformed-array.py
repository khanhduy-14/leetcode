class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for i in range(len(nums)):
            result_i = (i + nums[i] + len(nums)) % len(nums)
            result[i] = nums[result_i]

        return result