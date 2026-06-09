class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nmax = nums[0]
        nmin = nums[0]
        for i in range(1, len(nums)):
            nmax = max(nmax, nums[i])
            nmin= min(nmin, nums[i])

        return (nmax-nmin) * k