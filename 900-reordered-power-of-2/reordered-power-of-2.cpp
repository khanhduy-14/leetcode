vector<int> permutation(int n) {
    string s = to_string(n);
    sort(s.begin(), s.end()); 
    vector<int> result;
    
    do {
        if (s[0] != '0') {
            result.push_back(stoi(s));
        }
    } while (next_permutation(s.begin(), s.end()));
    
    return result;
}

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        vector<int> perms = permutation(n);
        for (int p : perms) {
            cout << p << endl;
            if ((p & (p-1)) ==0) {
                return true;
            } 
        }
        return false;
    }
};