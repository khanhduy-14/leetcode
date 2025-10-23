class Solution {
public:
    bool hasSameDigits(string s) {
        
        while (s.length() > 2) {
            string temp = "";
            for (int i = 0; i < s.length() - 1; i++) {
                temp+= ((s[i] - '0' +  s[i+1] - '0') % 10);
            }
            s = temp;
        }
        return s[0] == s[1];
    }
};