from collections import defaultdict, deque


class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # ----------------------------
        # Build prime table (sieve)
        # ----------------------------
        mx = max(nums)

        is_prime = [True] * (mx + 1)

        if mx >= 0:
            is_prime[0] = False
        if mx >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= mx:
            if is_prime[p]:
                for j in range(p * p, mx + 1, p):
                    is_prime[j] = False
            p += 1

        # ----------------------------
        # Build:
        # prime -> indices divisible by prime
        # ----------------------------
        mp = defaultdict(list)

        for i, x in enumerate(nums):

            # factorize x
            d = 2

            while d * d <= x:
                if x % d == 0:
                    mp[d].append(i)

                    while x % d == 0:
                        x //= d

                d += 1

            # remaining prime
            if x > 1:
                mp[x].append(i)

        # ----------------------------
        # BFS
        # ----------------------------
        q = deque([0])

        visited = [False] * n
        visited[0] = True

        steps = 0

        while q:

            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return steps

                # move left
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                # move right
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                # teleport
                val = nums[i]

                if is_prime[val]:

                    for nxt in mp[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    # IMPORTANT:
                    # don't use same teleport again
                    mp[val].clear()

            steps += 1