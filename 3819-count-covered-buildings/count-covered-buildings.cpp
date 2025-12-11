class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        vector<pair<int, int>> xBoundaries, yBoundaries;
        xBoundaries.resize(n+1, {n+1, 0});
        yBoundaries.resize(n+1, {n+1, 0});

        for (auto b : buildings) {
            xBoundaries[b[1]].first = min(xBoundaries[b[1]].first, b[0]);
            xBoundaries[b[1]].second = max(xBoundaries[b[1]].second, b[0]);
            yBoundaries[b[0]].first = min(yBoundaries[b[0]].first, b[1]);
            yBoundaries[b[0]].second = max(yBoundaries[b[0]].second, b[1]);
        }


       int res = 0;
       for (auto b : buildings) {
            if (b[0] > xBoundaries[b[1]].first
                && b[0] < xBoundaries[b[1]].second 
                && b[1] > yBoundaries[b[0]].first
                && b[1] < yBoundaries[b[0]].second
            ) res++;
       }
       
       return res;

    }
};