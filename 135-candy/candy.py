class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1 
        res = candy[n-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i+1] + 1, candy[i])
            res += candy[i]  
        return res

        