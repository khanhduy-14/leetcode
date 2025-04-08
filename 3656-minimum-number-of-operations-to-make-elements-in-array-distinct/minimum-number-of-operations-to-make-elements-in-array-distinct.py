class Solution:
    def minimumOperations(self, nums):
        mpp = [0] * 101
        for i in range(len(nums) - 1, -1, -1):
            mpp[nums[i]] += 1
            if mpp[nums[i]] == 2:
                return (i + 3) // 3
        return 0