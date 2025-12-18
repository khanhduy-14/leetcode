class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        long long base_profit = 0, window_base_profit = 0, window_profit_gain = 0;
        vector<long long> prefix_sum(n, 0), prefix_base_profit(n, 0);
        prefix_sum[0] = prices[0];
        prefix_base_profit[0] =  prices[0] * strategy[0];
        for (int i = 0 ; i < n; i++) {
            base_profit += (prices[i] * strategy[i]);
            if (i < k) {
                window_base_profit  = base_profit;
                if (i >= k/2) {
                    window_profit_gain+= prices[i];
                }
            }
         
        }
        long long gain_profit = max(1LL * 0, window_profit_gain - window_base_profit);
        for (int left = 1; left <= (n-k); left++) {
            window_base_profit-= (prices[left-1] * strategy[left-1]);
            window_base_profit+= (prices[left+k-1] * strategy[left+k-1]);
            window_profit_gain-=prices[left+k/2 - 1];
            window_profit_gain+=prices[left+k - 1];
            gain_profit = max(gain_profit, window_profit_gain - window_base_profit);
        }

        return base_profit + gain_profit;
        
    }
};