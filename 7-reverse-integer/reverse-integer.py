class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = [1, -1][x < 0]
        x = abs(x)
        while x:
            rev = rev * 10 + x % 10
            if rev > 2**31 - 1:
                return 0
            x = x // 10
        return rev * sign