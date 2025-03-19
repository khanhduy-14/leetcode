class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = nums[i] ^ 1
                nums[i+1] = nums[i+1] ^ 1
                nums[i+2] = nums[i+2] ^ 1
                res+=1
        return res if nums[-1] == 1 and nums[-2] == 1 else -1

        