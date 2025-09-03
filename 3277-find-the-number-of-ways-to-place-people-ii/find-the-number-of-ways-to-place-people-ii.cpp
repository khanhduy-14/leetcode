class Solution {
public:
    static bool comp(vector<int>&a, vector<int>&b) {
        if(a[0] == b[0]) {
            return a[1] > b[1];
        }
        return a[0] < b[0];
    }
    int numberOfPairs(vector<vector<int>>& points) {
        sort(points.begin(), points.end(),comp);

        int ans=0;
        for (int i = 0; i< points.size(); i++) {
            int y0 =  points[i][1];
            int miny = INT_MIN;
            for (int j=i+1; j<points.size(); j++) {
                 int y1 =  points[j][1];
                 if (y0 >= y1) {
                    if (y1 > miny) {
                        ans+=1;
                        miny=y1;
                    }
                 }
            }
        } 
        return ans;
    }
};