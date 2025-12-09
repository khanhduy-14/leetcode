const int MOD = 1e9 + 7;
class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        long long prevPairs[100001] = {0}, prevFreq[100001] = {0}, limit = 50000;
        long long res = 0;

        for (int num: nums) {
            
            if(num%2==0) {
                res = (res + prevPairs[num/2]);
            }

            if (num <= limit) {
                prevPairs[num]+=prevFreq[num*2];
            } 

            prevFreq[num]+=1;
        }
        return res % MOD; 
    }
};