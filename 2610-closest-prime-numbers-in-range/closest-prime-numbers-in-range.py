class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True] * (right + 1)
        def sieveOfEratosthenes():
            for num in range(2, right+1):
                if prime[num] == True and num * num <= right:
                    for i in range(num * num, right+1, num):
                        prime[i] = False
        sieveOfEratosthenes() 
        res = [-1,-1]
        selected_primes = []
        for i in range(max(left,2), right+1):
            if prime[i]:
                selected_primes.append(i)
        for i in range(1, len(selected_primes)):
            if res[0] == res[1] == -1:
                res[1] = selected_primes[i]
                res[0] = selected_primes[i-1]
                continue
            if selected_primes[i] - selected_primes[i-1] < res[1] - res[0]:
                res[1] = selected_primes[i]
                res[0] = selected_primes[i-1]
        print(selected_primes)
        return res

