class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        int gm = basket1[0];
        map<int, int> m;
        for (int c : basket1) {
            m[c] +=1;
            gm = min(c, gm);
        }
        for (int c : basket2) {
            m[c] -=1;
            gm = min(c, gm);
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