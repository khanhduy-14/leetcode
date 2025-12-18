class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<long long> prefix_sum(n, 0), prefix_base_profit(n, 0);
        prefix_sum[0] = prices[0];
        prefix_base_profit[0] =  prices[0] * strategy[0];
        for (int i = 1 ; i < n; i++) {
            prefix_sum[i] = prices[i] + prefix_sum[i-1];
            prefix_base_profit[i] =  (prices[i] * strategy[i]) + prefix_base_profit[i-1];
        }

        long long gain_profit = 0;

        for (int left = 0; left <= (n-k); left++) {
            int right = left + k - 1;
            int mid = left + ((k-1) / 2);
            int base_profit = prefix_base_profit[right] - (left > 0 ? prefix_base_profit[left-1] : 0);
            gain_profit = max(gain_profit, (prefix_sum[right] - prefix_sum[mid])  - base_profit);

        }

        return prefix_base_profit[n-1]+ gain_profit;
        
    }
};