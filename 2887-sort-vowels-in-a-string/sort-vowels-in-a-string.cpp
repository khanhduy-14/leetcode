class Solution {
public:
    string sortVowels(string s) {
        vector <char> arr;
        for (int i = 0; i < s.size(); i++) {
           char  c = static_cast<char>(s[i]);
           char lowerc = tolower(c);
           if (lowerc == 'a' || lowerc == 'u' || lowerc == 'e' || lowerc == 'o' || lowerc == 'i') {
            arr.push_back(c);
           }
        }
        sort(arr.begin(), arr.end());
        for (int i = s.size() - 1; i >= 0; i--) {
           char  c = static_cast<char>(s[i]);
           char lowerc = tolower(c);
           if (lowerc == 'a' || lowerc == 'u' || lowerc == 'e' || lowerc == 'o' || lowerc == 'i') {
             char last = arr.back();  
             arr.pop_back();     

             s[i] = last;
           }
        }
        return s;

    }
};