class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0;
        s = s.strip()

        if not s:
            return 0
        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        for i in range(len(s)):
            if not s[i].isnumeric():
                   break;
            if s[i].isnumeric():
                result = result * 10 + int(s[i])
                if sign > 0 and result > 2**31 - 1:
                    result = 2 ** 31 - 1
                if sign < 0 and result > 2**31:
                    result = 2 ** 31
        return sign * result