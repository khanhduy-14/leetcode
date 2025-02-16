class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum = 0

        for i in range(len(nums)):
            a = nums[i-k] if i-k >= 0 else 0
            b = nums[i+k] if i+k < len(nums) else 0
                        
            if nums[i] > a and nums[i] > b:
                sum+= nums[i]

        return sum
        