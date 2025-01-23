class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        absX = abs(x)
        while absX:
            rev = rev * 10 + absX % 10
            absX = absX // 10
            if rev > 2**31 - 1:
                return 0
        if x < 0:
            rev = -abs(rev)
        return rev