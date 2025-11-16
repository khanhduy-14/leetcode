static const long long MOD = 1'000'000'007LL;
class Solution {
public:
    int numSub(string s) {
       

        
        return cal(s);
        
    }
private: 
    long long cal(string s) {
        long long res = 0,add = 0;
        for (char c: s) {
            if (c=='0') add =0;
            else res+=++add;
        }
        return res%MOD;
    }
};