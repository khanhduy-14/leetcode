class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        pos_bit, n = [-1] * 30, len(nums)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(30):
                if nums[i] & (1 << bit) == 0:
                    if pos_bit[bit] != -1:
                        j = max(j, pos_bit[bit])
                else:
                    pos_bit[bit] = i
            res[i] = j - i + 1
        return res