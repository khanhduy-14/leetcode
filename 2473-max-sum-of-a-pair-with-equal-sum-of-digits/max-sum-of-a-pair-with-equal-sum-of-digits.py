class Solution:
    def sumOfDigits(self,n: int):
        sum = 0
        while n != 0:
            last = n % 10
            sum += last
            n //= 10
        return sum
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        map = {}
        for i in range(len(nums)):
            sumDigits = self.sumOfDigits(nums[i])
            if sumDigits in map:
                if nums[map[sumDigits]] + nums[i] > max_sum:
                    max_sum = nums[map[sumDigits]] + nums[i]
                if nums[i] > nums[map[sumDigits]]:
                    map[sumDigits] = i
            else:
                map[sumDigits] = i 
        return max_sum