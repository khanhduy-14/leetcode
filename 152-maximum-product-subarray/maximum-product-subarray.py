class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        min_product = nums[0]
        max_product = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                min_product, max_product = max_product, min_product
            max_product = max(nums[i], max_product *nums[i])
            min_product = min(nums[i], min_product * nums[i])
            res = max(res, max_product)
        return res
