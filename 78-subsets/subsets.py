class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtracking(i+1, subset)
            subset.pop()
            backtracking(i+1, subset)
        backtracking(0, [])
        return res
        