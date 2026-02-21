class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1, n+1):
            prev = pow(2, math.floor(math.log2(i)))
            ans[i] = 1 + ans[i - prev]
        
        return ans