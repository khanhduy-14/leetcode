class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n,m,curr_sum, curr_query = len(nums), len(queries),0,0
        d = [0  for i in range(0, n+1)]

        for i in range(n):
            curr_sum+=d[i]
            while curr_query < m and curr_sum < nums[i]:
                l,r,v = queries[curr_query]
                print(l,r,v,curr_sum)
                if i < l:
                    d[l]+=v
                elif i <= r:
                    curr_sum+=v
                d[r+1]-=v
                curr_query+=1
                print(curr_sum)
            if curr_sum < nums[i]:
                return -1

        return curr_query
        