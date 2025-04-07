class Solution:
    def rob(self, nums: List[int]) -> int:
        prevs, maxs = 0, 0

        for i in range(len(nums)):
            if prevs + nums[i] > maxs:
                temp = prevs + nums[i]
                prevs = maxs
                maxs = temp
            else:
                prevs= maxs
                
        return maxs




        
        