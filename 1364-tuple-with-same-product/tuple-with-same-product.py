class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        map = {}
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] * nums[j]) in map:
                    res+=(map[nums[i] * nums[j]] * 8)
                    map[nums[i] * nums[j]]+=1
                else:
                    map[nums[i] * nums[j]]=1
       
        return int(res)