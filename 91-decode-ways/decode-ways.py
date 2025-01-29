class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        prevWays = 0
        if s[0] == '0':
            return 0
        for i in range(len(s)):
            if i == 0 and  1 <= int(s[i]) <= 9:
                ways+=1
                continue;

            if s[i] == '0':
                if 1 <= int(s[i-1:i+1]) <= 26:
                    ways-=prevWays
                    prevWays = ways
                else:
                    return 0
                continue
            if 1 <= int(s[i-1:i+1]) <= 26 and s[i-1] !=0:
                addedWays = ways - prevWays
                ways+= addedWays
                prevWays = addedWays
            else:
                prevWays = 0

        return ways