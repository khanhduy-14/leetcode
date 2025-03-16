class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if len(nums) == 1:
            return 0

        def isValid(i):
            if i >= 0 and i < len(nums):
                v = nums[i]
                lv = -2**31 if i - 1 < 0 else nums[i-1]
                rv = -2**31 if i + 1 >= len(nums) else nums[i+1]

                return v>= lv and v>=rv

        while l < r:
            m = (l+r)//2
            if isValid(l):
                return l
            else:
                l+=1
            if isValid(r):
                return r
            else:
                r+=1
            if isValid(m):
                return m
            elif nums[m+1] >= nums[m]:
                l = m+1
            else:
                r = m
        return -1




        
        