class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        map = {value: index for index, value in enumerate(arr)}
        print(map)
        res = 0
        dp = [[0] * len(arr) for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            for j in range(len(arr) - 1, i,-1):
               nxt = arr[i] + arr[j]
               length = 2
               if nxt in map: 
                    length = 1 + dp[j][map[nxt]]
                    res = max(res, length)
               dp[i][j] = length
        return res