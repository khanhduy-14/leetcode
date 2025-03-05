class Solution:
    def coloredCells(self, n: int) -> int:
        if n<=1:
            return n

        return 1 + int(4 * ((n-1) * n / 2))
