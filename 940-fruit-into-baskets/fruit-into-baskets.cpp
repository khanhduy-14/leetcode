class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int l = 0, r = 0, ans = 0;
        map <int, int> m;
        for (r; r < fruits.size(); r++) {
            m[fruits[r]]+=1;

            while (m.size() > 2) {
                m[fruits[l]]-=1;
                if (m[fruits[l]] == 0) m.erase(fruits[l]);
                l++;
            }
            ans = max(ans, r - l + 1);

        }
        return ans;
    }
};