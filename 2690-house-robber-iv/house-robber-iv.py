class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValid(capability: int):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count+=1
                    i+=2
                else:
                    i+=1
                if count == k:
                    break
            return count==k
        l,r = min(nums), max(nums)
        while l < r:
            m = (l+r) //2
            if isValid(m):
                r=m
            else:
                l=m+1
        return l

        return res

        