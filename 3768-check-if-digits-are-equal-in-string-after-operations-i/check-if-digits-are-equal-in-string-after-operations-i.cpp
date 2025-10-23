class Solution {
public:
    bool hasSameDigits(string s) {
        
        while (s.length() > 2) {
            string temp = "";
            for (int i = 0; i < s.length() - 1; i++) {
                int c1 = (int) s[i], c2 = (int) s[i+1];
                temp+= ((c1+c2) % 10);
            }
            s = temp;
        }
        return s[0] == s[1];
    }
};