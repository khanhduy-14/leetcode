class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        x = heapq.heappop(nums)
        while x < k:
            res += 1
            y = heapq.heappop(nums)
            newNum = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, newNum)
            x = heapq.heappop(nums)
        return res
        

