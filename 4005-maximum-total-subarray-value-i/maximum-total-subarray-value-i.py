class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nmax = nmin = nums[0] 
        for num in nums:
            nmax = max(nmax, num)
            nmin = min(nmin, num)

        return (nmax-nmin) * k