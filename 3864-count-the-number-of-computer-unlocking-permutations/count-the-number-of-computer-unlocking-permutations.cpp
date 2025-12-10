const int MOD = 1e9+7;
class Solution {
public:
    long long factorial(int n) {
        long long res = 1;
        for (int i = 2; i <= n; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }

    int countPermutations(vector<int>& complexity) {
        int n = complexity.size();

        for (int i = 1; i < n; i++) {
            if(complexity[0] >= complexity[i]) {
                return 0;
            }
        }

        return factorial(n-1) % MOD;
         
    }
};