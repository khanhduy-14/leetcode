from typing import List
import heapq
from math import log2

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        st_max = [[0] * m for _ in range(n)]
        st_min = [[0] * m for _ in range(n)]

        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << (j - 1)

            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(
                    st_max[i][j - 1],
                    st_max[i + length][j - 1]
                )

                st_min[i][j] = min(
                    st_min[i][j - 1],
                    st_min[i + length][j - 1]
                )

            j += 1

        def value(l: int, r: int) -> int:
            p = lg[r - l + 1]

            mx = max(
                st_max[l][p],
                st_max[r - (1 << p) + 1][p]
            )

            mn = min(
                st_min[l][p],
                st_min[r - (1 << p) + 1][p]
            )

            return mx - mn

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            ans += -neg_v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans