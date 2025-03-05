class Solution:
    def coloredCells(self, n: int) -> int:
        if n<=1:
            return n
        dp = 1

        for i in range(1,n):
            dp += 4 * i
        
        return dp
