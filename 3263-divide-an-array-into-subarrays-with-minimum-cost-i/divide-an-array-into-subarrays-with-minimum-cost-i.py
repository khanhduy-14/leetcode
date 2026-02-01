class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1 = 51
        min_2 = 51
        for i in range(1, len(nums)):
            if nums[i] < min_1:
                min_2 = min_1
                min_1 = nums[i]
            elif nums[i] < min_2:
                min_2 = nums[i]
            
            if min_1 == 1 and min_2 == 1:
                break 
        return nums[0] + min_1 + min_2