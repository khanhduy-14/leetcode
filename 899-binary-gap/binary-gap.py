class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        curr = 0
        while n:
            if n & 1:
                res = max(res, curr)
                curr = 0
                curr+=1

            else:
                if curr:
                    curr+=1
            n = n >> 1
        return res
        