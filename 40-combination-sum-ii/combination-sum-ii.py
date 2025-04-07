class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def backtracking(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            j = i
            while j < len(candidates):
                curr.append(candidates[j])
                backtracking(j+1, curr, total + candidates[j])
                curr.pop()
                while j+1< len(candidates) and candidates[j] == candidates[j+1]:
                    j= j+1
                j+=1

        backtracking(0, [], 0)
        return res