

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        string s = to_string(n);
        sort(s.begin(), s.end());
       
        for (int i = 0; i < 30; i++) {
            int p2 = 1 << i;
            string p2str = to_string(p2);
            sort(p2str.begin(), p2str.end());
            if(p2str== s) {
                return true;
            }
        }
        return false;
    }
};