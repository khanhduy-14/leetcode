class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtracking(i, curr_arr, total):
            if total == target:
                res.append(curr_arr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            for j in range(i, len(candidates)):
                curr_arr.append(candidates[j])
                backtracking(j, curr_arr, total + candidates[j])
                curr_arr.pop()

        backtracking(0, [], 0)
        return res