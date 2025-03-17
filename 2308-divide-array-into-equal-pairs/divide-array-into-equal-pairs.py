class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        n = len(nums)
        for i in range(n):
            if len(s) > (n- i):
                return False
            if nums[i] in s:
                s.remove(nums[i])
            else:
                s.add(nums[i])
        return len(s) == 0
        