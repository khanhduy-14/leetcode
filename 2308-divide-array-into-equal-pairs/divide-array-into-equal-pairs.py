class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in s:
                s.remove(nums[i])
            else:
                s.add(nums[i])
            if len(s) > (n- i -1):
                return False
        return len(s) == 0
        