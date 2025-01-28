class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            lastValue = res[len(res) - 1][1]
            if intervals[i][0] <= res[len(res) - 1][1]:
               res[len(res) - 1][1] = max(intervals[i][1], res[len(res) - 1][1])
            
            else:
                res.append(intervals[i])
        
        return res
        