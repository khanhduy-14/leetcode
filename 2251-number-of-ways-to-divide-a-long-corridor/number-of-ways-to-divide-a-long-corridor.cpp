const int MOD = 1e9+7;
class Solution {
public:
    int numberOfWays(string corridor) {
        int n = corridor.size();
        long long res = 1;
        vector<int> seatPos;

        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') {
                seatPos.push_back(i);
            }
        }
        int nSeat = seatPos.size();
        if (nSeat % 2 || nSeat == 0) {
            return 0;
        }

        for (int i = nSeat - 2; i > 0 ; i=i-2) {
            res= ((seatPos[i] - seatPos[i-1]) * res) % MOD;
        }

        return res % MOD;
        
    }
};