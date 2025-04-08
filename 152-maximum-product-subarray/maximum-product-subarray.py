class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp, minp, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxp, minp = minp, maxp
            maxp = max(maxp*nums[i], nums[i])
            minp = min(minp*nums[i], nums[i])
            res = max(maxp, res)

        return res