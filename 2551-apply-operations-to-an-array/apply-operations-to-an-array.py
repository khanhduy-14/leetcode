class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        cur = 0
        for i in range(len(nums)):
            num = nums[i]
            if i < len(nums) - 1 and  num == nums[i+1]:
                num *=2
                nums[i+1] = 0
                nums[i] = num
            if num != 0:
                res[cur] = num
                cur+=1
        return res


        