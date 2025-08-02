class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res, max_or, mask, n = 0, 0, 0, len(nums)
        for num in nums:
            max_or |= num

        while mask < (1 << n):
            or_subset = 0
            for i in range(n):
                if mask & (1 << i):
                   or_subset = or_subset | nums[i]
            if or_subset == max_or:
                res+=1
            
            mask+=1
        return res