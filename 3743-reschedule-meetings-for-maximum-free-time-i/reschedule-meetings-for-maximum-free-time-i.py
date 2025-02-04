class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeTime = []
        freeTime.append(startTime[0])
        maxTime = 0
        currTime = 0
        for i in range(1, len(startTime)):
            freeTime.append(startTime[i] - endTime[i-1])
        
        freeTime.append(eventTime - endTime[-1])
      
        currTime = sum(freeTime[0:k + 1])
        maxTime = sum(freeTime[0:k + 1])
        l = 1
        while  l+k < len(freeTime):
            currTime-= freeTime[l-1]
            currTime+= freeTime[l+k]
            maxTime = max(currTime, maxTime)
            l+=1
            
        return maxTime
