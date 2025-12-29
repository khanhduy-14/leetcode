class Solution {
public:
    unordered_map<string, vector<char>> mp;
    unordered_map<string, bool> memo;

    bool dfs(string& bottom) {
        if (bottom.size() == 1)
            return true;























            
        if (memo.count(bottom)) {
            return memo[bottom];
        }

        string nextRow;
        return memo[bottom]=buildNextRow(bottom, 0, nextRow);
    }

    bool buildNextRow(string &bottom, int index, string &nextRow) {
        if (index == bottom.size() - 1) {
            return dfs(nextRow);
        }

        string key  = bottom.substr(index, 2);

        for (auto c : mp[key]) {
            nextRow.push_back(c);
            if(buildNextRow(bottom, index+1, nextRow)) {
                return true;
            }
            nextRow.pop_back();
        }

        return false;
    }
    
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        for (string a : allowed) {
            mp[a.substr(0, 2)].push_back(a[2]);
        }
        return dfs(bottom);
    }
};