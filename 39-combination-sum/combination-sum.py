class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtracking(i, curr_arr):
            if sum(curr_arr) == target:
                res.append(curr_arr.copy())
                return
            if i >= len(candidates) or sum(curr_arr) > target:
                return
            for j in range(i, len(candidates)):
                curr_arr.append(candidates[j])
                backtracking(j, curr_arr)
                curr_arr.pop()

        backtracking(0, [])
        return res