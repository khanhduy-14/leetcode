class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        l,r = 0, len(nums)-1
        i_nev, i_pos = -1, -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < 0 and (m == len(nums) - 1 or  nums[m+1] >=0):
                i_nev = m
                break
            elif nums[m] >= 0:
                r=m-1
            else:
                l=m+1
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > 0 and ( m==0 or nums[m-1] <=0):
                i_pos = m
                break
            elif nums[m] <= 0:
                l=m+1
            else:
                r=m-1
        return max(i_nev + 1, len(nums) - i_pos if i_pos != -1 else 0) 


        