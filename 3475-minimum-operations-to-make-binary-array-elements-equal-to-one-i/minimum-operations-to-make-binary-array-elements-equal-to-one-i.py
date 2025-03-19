class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            if i+2 >= len(nums):
                continue
            res+=1
            for j in range(i, i+3):
                nums[j] = nums[j] ^ 1
        return res if sum(nums) == len(nums) else -1

        