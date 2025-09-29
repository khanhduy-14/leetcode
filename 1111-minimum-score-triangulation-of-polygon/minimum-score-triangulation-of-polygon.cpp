class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        // top down
        // int N = values.size();
        // vector<vector<int>> memo(N, vector<int>(N, -1));

        // function<int(int, int)> dp = [&] (int i, int j) -> int {
        //     if (j-i < 2) return 0;
        //     if (memo[i][j] != -1) return memo[i][j]; 
        //     if (j-i == 2) return values[i] * values[i+1] * values[i+2];
        //     int res = INT_MAX;
        //     for (int k = i+1; k<j;k++) {
        //         res = min(res, values[k] * values[i] * values[j] + dp(i,k) + dp(k,j));
        //     }
        //     return memo[i][j] = res;
        // };
        // int res = dp(0, values.size() - 1);
        // return res;

        // bottom up

        int N = values.size();
        vector<vector<int>> dp(N, vector<int>(N, 0));

        for (int u = 3; u < N + 1; u++) {
            for (int i = 0; i < N - u + 1; i++){
                int j = i + u - 1;
                dp[i][j] = INT_MAX;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = min(dp[i][j], values[k] * values[i] * values[j] + dp[i][k] + dp[k][j]);
                }
            }
        }
        return dp[0][N-1];

    }
};