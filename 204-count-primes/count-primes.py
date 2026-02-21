class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        x = [True] * n
        res = 0
        for i in range(2, n):
            if x[i] == True:
                res+=1
                j = i * i
                while j < n:
                    x[j] = False
                    j+=i
        
        return res