const int MOD = 1e9+7;
class Solution {
public:
    int numberOfWays(int n, int x) {
        vector<int> aux;
        int temp = 1;
        while ((int)pow(temp,x) <= n) {
            aux.push_back((int)pow(temp,x));
            temp+=1;
        }
        vector<int> dp(n+1, 0);
        dp[0] = 1;

        for(int num: aux) {
            for(int i = n; i>= num; i--) {
                dp[i] = (dp[i] + dp[i - num]) % MOD;
            }
        }
        return dp[n];
    }
};