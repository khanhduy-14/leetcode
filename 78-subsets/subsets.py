class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        def backtracking(index: int):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[index])

            backtracking(index + 1)

            subset.pop()
            backtracking(index + 1)
        
        backtracking(0)

        return res
        