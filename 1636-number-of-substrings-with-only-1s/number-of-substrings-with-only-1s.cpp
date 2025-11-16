static const long long MOD = 1'000'000'007LL;
class Solution {
public:
    int numSub(string s) {
        vector<string> arr1 = split(s, "0");
        long long res = 0;
        for (string str1 : arr1) {
            long long len = (long long)str1.size();
            long long add = (len * (len + 1)) / 2;  // safe
            res = (res + add) % MOD;
        }
        return res;
        
    }
private: 
    vector<string> split(string s, string delimiter) {
        vector<string> arr;
        int start=0, end;
        while((end = s.find(delimiter, start)) != string::npos) {
            arr.push_back(s.substr(start, end - start));
            start= end + 1;
        }
        arr.push_back(s.substr(start, s.size() - start));

        return arr;
    }
};