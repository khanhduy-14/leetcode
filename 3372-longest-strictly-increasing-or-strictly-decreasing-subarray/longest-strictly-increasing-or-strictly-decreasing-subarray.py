class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_asc = 1
        max_dsc = 1
        res = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_asc+=1
                max_dsc=1
            elif nums[i] < nums[i-1]:
                max_dsc+=1
                max_asc=1
            else:
                 max_asc=1
                 max_dsc=1
            res = max(max_dsc, max_asc, res)

        return res