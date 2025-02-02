class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gasTank = 0
        currGasTank = 0
        startIndex = 0
        for i in range(len(gas)):
            gasTank += (gas[i] - cost[i])
            currGasTank  += (gas[i] - cost[i])
            if currGasTank < 0:
                startIndex = i + 1
                currGasTank = 0

        return -1 if gasTank < 0 else startIndex