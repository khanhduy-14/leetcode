class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        map = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] * nums[j]) in map:
                    map[nums[i] * nums[j]]+=1
                else:
                    map[nums[i] * nums[j]]=1
        res = 0
        for key in map:
            if map[key] > 1:
                numPair = (map[key] * (map[key] - 1)) / 2
                numPair *=8
                res+=numPair
        return int(res)