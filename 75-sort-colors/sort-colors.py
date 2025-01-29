class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArr= [0 for _ in range(3)]
        for i in range(len(nums)):
            countArr[nums[i]]+=1
        
        idx = 0

        for i in range(len(countArr)):
            nums[idx:idx+countArr[i]]= [i] * countArr[i]
            idx+= countArr[i]
        
        return nums

        