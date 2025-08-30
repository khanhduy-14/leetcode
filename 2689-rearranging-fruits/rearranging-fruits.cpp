class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        int gm = basket1[0];
        unordered_map<int, int> m;
        for (int i = 0; i < basket1.size(); ++i) {
            m[basket1[i]]++;
            m[basket2[i]]--;
            gm = min(gm, min(basket1[i], basket2[i]));
        }

        vector<int> swp;
        for (auto &p : m) {
            if (p.second % 2 != 0) return -1;

            for(int i = 0; i < abs(p.second) / 2; i++) {
                cout << p.first << " "  << p.second << endl;
                swp.push_back(p.first);
            }
        }
        sort(swp.begin(), swp.end());
     
        long long c = 0;
        for (int i = 0; i < swp.size() / 2; i++) {
            int dc = swp[i];
            int idc = gm * 2;
            c+= min(dc,idc);
        }
        return c;
        
    }
};