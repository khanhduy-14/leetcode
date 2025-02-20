class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = list(nums[0])
        for i in range(len(nums)):
            res[i] = "1" if nums[i][i] == "0" else "0"
        return ''.join(res)
        