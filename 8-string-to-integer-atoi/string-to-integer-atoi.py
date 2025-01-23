class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1;
        result = 0;
        isRead = False
        s = s.strip()
        for i in range(len(s)):
            if not s[i].isnumeric():
                if isRead:
                   break;
                if s[i] != '+' and s[i] != '-':
                    break;
            if s[i] == '-':
                sign = -1
           
            if s[i] == '+':
                sign = 1
            if s[i].isnumeric():
                result = result * 10 + int(s[i])
                print(result)
                if sign > 0 and result > 2**31 - 1:
                    result = 2 ** 31 - 1
                if sign < 0 and result > 2**31:
                    result = 2 ** 31
            isRead = True
        return sign * result