class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp, minp = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            
            tmax= maxp
            tmin= minp
            maxp = max(tmax*nums[i], tmin * nums[i], nums[i])
            minp = min(tmax*nums[i], tmin * nums[i], nums[i])
            res = max(maxp, res)

        return res