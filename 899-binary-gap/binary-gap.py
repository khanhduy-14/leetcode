class Solution:
    def binaryGap(self, n: int) -> int:
        if (n & (n - 1)) == 0: return 0
        n //= (n & -n)
        res = 0
        curr = 0
        while n:
            if n & 1:
                res = max(res, curr)
                curr = 1
            else:
                curr+=1
            n = n >> 1
        return res
        