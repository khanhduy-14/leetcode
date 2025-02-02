class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                k+=1
        
        if k == 0:
            return True
        if k == 1 and nums[0] >= nums[-1]:
            return True
        return False
