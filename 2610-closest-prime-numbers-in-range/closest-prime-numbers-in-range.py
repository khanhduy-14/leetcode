class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True] * (right + 1)
        prime[0] = prime[1] = False
        for num in range(2, right+1):
            if prime[num] == True and num * num <= right:
                for i in range(num * num, right+1, num):
                    prime[i] = False
        res = [-1,-1]
        selected_primes = []
        
        for i in range(left, right+1):
            if prime[i]:
                selected_primes.append(i)
        if len(selected_primes) < 2:
            return res
        for i in range(1, len(selected_primes)):
            if selected_primes[i] - selected_primes[i-1] < res[1] - res[0] or res[0] == -1:
                res = [selected_primes[i-1],selected_primes[i]]
        return res

