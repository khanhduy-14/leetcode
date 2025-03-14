class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sc,l,r = sum(candies),1,max(candies)

        while l <= r:
            m = (l + r)//2
            if m > sc:
                r = m - 1
                continue
            temp = k
            for x in candies:
                if x < m: 
                    continue
                temp-=(x//m)
            if temp <= 0:
                l = m + 1
            else: 
                r = m - 1
        return r
