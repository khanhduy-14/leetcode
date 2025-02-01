class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freeTime = []
        freeTime.append(startTime[0])
        maxTime = 0
        currTime = 0
        for i in range(1, len(startTime)):
            freeTime.append(startTime[i] - endTime[i-1])
        
        freeTime.append(eventTime - endTime[-1])
      

        prefix = [0]
        for i in range(1,len(startTime)):
            pr = prefix[-1]
            prefix.append(max(pr, freeTime[i - 1]))
        suffix = [0]
        for i in range(len(startTime) - 2, -1, -1):
            su = suffix[-1]
            suffix.append(max(su, freeTime[i+2]))
        suffix = suffix[::-1]
        

        print(freeTime, prefix, suffix)
        
        for i in range(len(startTime)):
            blockSize = endTime[i] - startTime[i]
            leftGap = freeTime[i]
            rightGap = freeTime[i+1]

            maxTime = max(maxTime, leftGap+rightGap)

            if max(prefix[i], suffix[i]) >= blockSize:
                maxTime = max(maxTime, leftGap+rightGap + blockSize)
        return maxTime