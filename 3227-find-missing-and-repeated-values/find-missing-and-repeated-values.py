class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set(list(range(1,( len(grid) * len(grid)) + 1)))
        d = 0
        rows,cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in s:
                    s.remove(grid[i][j])
                else:
                   d = grid[i][j]
        return [d] + list(s)
        