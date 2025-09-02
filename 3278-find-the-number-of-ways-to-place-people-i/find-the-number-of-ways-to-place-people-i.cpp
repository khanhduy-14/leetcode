class Solution {
public:
    static bool comp (vector<int>& a, vector<int>& b) {
        if (a[0] == b[0]) 
            {
                return a[1] > b[1];
            }
        return a[0] < b[0];
    }
    int numberOfPairs(vector<vector<int>>& points) {
        int ans = 0;
        sort(points.begin(), points.end(), comp);
        for (int i = 0; i < points.size(); i++) {
             vector<int> a = points[i];
             int miny = INT_MIN; 
            for (int j = i+1; j < points.size(); j++) {
                vector<int> b = points[j];
                if (a[1] >= b[1]) {
                    if (b[1] > miny) {
                        ans+=1;
                        miny =  b[1];
                    }
                }
            }
        }
        return ans;
    }
};