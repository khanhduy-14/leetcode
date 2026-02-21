class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        x = [True] * n
        x[0] = x[1] = False
        for i in range(3, int(n**0.5) + 1, 2):
            if x[i]:
                j = i * i
                while j < n:
                    x[j] = False
                    j+=(2*i)
        return 1 + sum(x[i] for i in range(3,n,2))