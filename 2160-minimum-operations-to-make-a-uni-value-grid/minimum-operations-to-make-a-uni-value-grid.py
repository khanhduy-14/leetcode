class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ov = [num for row in grid for num in row]
        ov.sort()
        dn = ov[len(ov) // 2]
        remainder = -1
        res = 0

        for row in grid:
            for num in row:
                if remainder != -1 and remainder != (num%x):
                    return -1
                remainder = num%x
                res+= (abs(num-dn) // x)

        return res