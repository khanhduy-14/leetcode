class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        nday,res = 1,0
        meetings.sort()
        for s,e in meetings:
            if nday < s:
                res += s - nday
            nday = max(e+1 , nday)
        if nday <= days:
            res += (days - nday + 1)
        return res
        