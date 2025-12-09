const int MOD = 1e9 + 7;
class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        unordered_map<int, long long> prevC = {}, totalC = {};

        for (int num:nums) {
            totalC[num] +=1;
        }
        long long res = 0;
        for (int num:nums) {
            res+= (prevC[num*2] * (totalC[num*2] - prevC[num*2] + (num == 0 ? -1 : 0)));
            prevC[num]+=1;
        }

        return res % MOD;
    }
};