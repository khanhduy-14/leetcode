class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, cur,res = 0, 0, 0
        
        for r in range(len(nums)):

           
            while cur & nums[r] != 0:
                    cur=cur^nums[l]
                    l+=1
            cur = cur | nums[r]
            res = max(res, r-l+1)
           


        return res
    