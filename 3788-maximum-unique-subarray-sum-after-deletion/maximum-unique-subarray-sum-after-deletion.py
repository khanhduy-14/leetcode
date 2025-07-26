class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res, s = 0, set()
        if max(nums) < 0:
            return max(nums)
        for num in nums:
            if num > 0 and num not in s:
                s.add(num)
                res+=num
        return res