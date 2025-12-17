class Solution {
public:

    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();
        vector<array<long long,3>> dp(k+1), tempDp(k+1);

        for(int i = 0; i <= k; i++) {
            dp[i][0] = -1e9;
            dp[i][1] = -1e9;
            dp[i][2] = -1e9;
        } 
        dp[0][0] = 0;

        

        for (int i = 0; i < n; i++) {
            tempDp = dp;
            for(int j = 0; j <=k ; j++) {
                
                dp[j][0] = tempDp[j][0];
                if (j >= 1) {
                    dp[j][0] = max({
                        tempDp[j][0],
                        tempDp[j-1][1] + prices[i],
                        tempDp[j-1][2] - prices[i]
                    });
                }

                dp[j][1] = max(tempDp[j][1], tempDp[j][0] - prices[i]);

                dp[j][2] = max(tempDp[j][2], tempDp[j][0] + prices[i]);
            }
        }

        long long ans = 0;

        for (int i = 1; i<=k; i++) {
            ans = max(ans, dp[i][0]);
        }

        return ans;

    }
};