class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        quotient = 0
        sign = 1
        if dividend < 0:
            sign *= -1
        if divisor < 0:
            sign *= -1  
        dividend = abs(dividend)
        divisor = abs(divisor)
        multiply = 1
        tempDivisor = divisor


        while tempDivisor<<1 < dividend:
            multiply<<=1
            tempDivisor<<=1
        while dividend >= divisor:
            if dividend >= tempDivisor:
                dividend -= tempDivisor
                quotient += multiply
                
            else:
                multiply>>=1
                tempDivisor>>=1
        
        return min(max(quotient * sign, -2 ** 31), 2 ** 31 -1)
        