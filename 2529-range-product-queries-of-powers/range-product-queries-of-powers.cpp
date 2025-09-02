const int MOD = 1e9 + 7;
class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> ans;
        vector<int> powers;

        int bit = 0;
        while (1<<bit <= n) {
            if ((n & (1<< bit)) != 0) {
                powers.push_back(1<<bit);
            }
            bit+=1;
        }
        

        for (int i = 0; i< queries.size(); i++) {
            if (queries[i][0] == queries[i][1]) {
                ans.push_back(powers[queries[i][0]] % MOD);
                continue;
            }
            long long tmp = 1;
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                tmp = (tmp * powers[j]) % MOD;
            }
            ans.push_back(tmp);
        }
        return ans;
    }
};