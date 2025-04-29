class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        max_val = 0
        for i, num in enumerate(nums):
            if num > max_val:
                arr = [i]
                max_val = num
            elif num == max_val:
                arr.append(i)

        if len(arr) < k:
            return 0
        
        l, r = 0, k - 1
        left_bound = -1
        res = 0
        while r < len(arr):
            res += (arr[l] - left_bound) * (len(nums) - arr[r])
            left_bound = arr[l]
            l += 1
            r += 1
        
        return res