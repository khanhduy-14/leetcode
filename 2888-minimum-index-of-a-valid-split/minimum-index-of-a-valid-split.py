class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m, cm = {},{}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        
        for i in range(len(nums)):
            cm[nums[i]] = cm.get(nums[i], 0)+1
            if cm[nums[i]] * 2 > i + 1 and (m[nums[i]] - cm[nums[i]]) * 2 > (len(nums) - 1 - i):
                return i
        return -1


        