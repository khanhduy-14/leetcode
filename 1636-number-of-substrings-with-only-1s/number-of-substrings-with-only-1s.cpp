static const long long MOD = 1'000'000'007LL;
class Solution {
public:
    int numSub(string s) {
       

        
        return cal(s);
        
    }
private: 
    long long cal(string s) {
        long long res = 0;
        int start=0, end;
        while((end = s.find("0", start)) != string::npos) {
            long long len = (long long)s.substr(start, end - start).size();
            long long add = (len * (len + 1)) / 2; 
            res = (res + add) % MOD;
            start= end + 1;
        }
            long long len = (long long)s.substr(start, s.size() - start).size();
            long long add = (len * (len + 1)) / 2; 
            res = (res + add) % MOD;
        return res;
    }
};