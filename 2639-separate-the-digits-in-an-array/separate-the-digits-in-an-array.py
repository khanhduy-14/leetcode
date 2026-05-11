class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - 1, -1 , -1):
            while nums[i] > 0:
                result.append(nums[i] % 10)
                nums[i] //=10
        result.reverse()
        return result