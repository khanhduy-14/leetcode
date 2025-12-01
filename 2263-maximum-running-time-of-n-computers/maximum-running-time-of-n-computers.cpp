class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long maxTime = accumulate(batteries.begin(), batteries.end(), 0LL) / n;
        long long minTime = 0;

        while(minTime<maxTime) {
           long long checkTime = (maxTime+ minTime +1) / 2;
           long long maxCharge = 0;
            for (int x : batteries) {
                maxCharge += min((long long)x, checkTime);
            }
            if(maxCharge >=  checkTime * n) {
                minTime=checkTime;
            }
            else {
                maxTime=checkTime - 1;
            }
        }
        return minTime;
        
    }
};