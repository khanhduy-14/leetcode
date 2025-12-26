class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size();
        vector<vector<int>> prefix(n + 2, vector<int>(2, 0));
        for (int i = 1; i <= n; i++) {
            prefix[i][0] = prefix[i-1][0] + (customers[i-1] == 'Y' ? 1 : 0);
            prefix[i][1] = prefix[i-1][1] + (customers[i-1] == 'N' ? 1 : 0);
        }

        pair<int, int> res = {0, 1e5};
        for (int i = 1; i <= n + 1; i++) {
            int penalty = prefix[i-1][1] + (prefix[n][0] - prefix[i-1][0]);
            if (penalty < res.second) {
                res.second = penalty;
                res.first = i;
            }
        }

        return res.first - 1;
    }
};