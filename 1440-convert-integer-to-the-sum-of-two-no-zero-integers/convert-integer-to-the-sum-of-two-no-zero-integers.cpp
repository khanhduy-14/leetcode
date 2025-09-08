class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        string nstr = to_string(n);
        if (nstr.size() == 1) {
            return {1, n-1};
        }

        string astr(nstr.size() -1, '0');

        for (int i = 1; i < nstr.size(); i++) {
            if (nstr[i] != '9') {
                astr[i-1]  = nstr[i] + 1;
            }
            else {
                astr[i-1] = '1';
            }
        } 
        int a = stoi(astr);
        return {a, n-a};
    }
};