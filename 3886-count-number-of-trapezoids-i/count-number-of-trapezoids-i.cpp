const int MOD = 1e9 + 7;
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map <int, int> hm = {};
        long long sameY2 = 0, sum = 0;
        for (auto point: points) {
            hm[point[1]]+=1;
        }

        for (const auto& [key, value] : hm) {
            if(value < 2) {
                continue;
            }
            long long pairs = 1LL * value * (value - 1) / 2;

            sameY2+= (pairs * pairs);
            sum+= pairs;
        }

        return ((sum * sum) - sameY2) / 2 % MOD;
    }
};
