class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique, l, c_sum, res = set(), 0, 0, 0

        for r in nums:
            while r in unique:
                c_sum -= nums[l]
                unique.remove(nums[l])
                l+=1
            c_sum += r
            unique.add(r)
            res = max(res, c_sum)
        
        return res

        