class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(fixedPosition): 
            if fixedPosition == len(nums):
                res.append(nums[:])
            
            for i in range(fixedPosition, len(nums)):
                nums[i], nums[fixedPosition] = nums[fixedPosition], nums[i]
                backtrack(fixedPosition + 1)

                # reset
                nums[i], nums[fixedPosition] = nums[fixedPosition], nums[i]

        backtrack(0)
        return res



