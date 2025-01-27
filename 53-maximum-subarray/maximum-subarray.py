class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = -sys.maxsize - 1
        sum = 0
        for i in range(0,len(nums)):
            if sum < 0:
                sum = 0
            sum+=nums[i]

            if sum >= maxSum:
                maxSum = sum
            
            if sum <= 0:
                sum = nums[i]
                
        return maxSum