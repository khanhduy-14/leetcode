class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size(), nCol = strs[0].size();
        vector<int> dp(nCol, 1);
        for (int i = 0; i < nCol; i++) {
            for (int j = 0; j < i; j++) {
                int is_valid = 1;
                for (int row = 0; row<n ; row ++) {
                    if (strs[row][j] > strs[row][i]) {
                        is_valid = 0;
                    }
                }
                if (is_valid == 1) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxDp = 0;
        for (int x : dp) maxDp = max(maxDp, x);

        return nCol - maxDp;
    }
};