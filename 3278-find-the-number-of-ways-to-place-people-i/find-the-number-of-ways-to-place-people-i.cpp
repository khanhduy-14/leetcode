class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int ans = 0;

        for (int i = 0; i < points.size(); i++) {
            vector<int> a = points[i];
            for (int j = 0; j < points.size(); j++) {
                vector<int> b = points[j];
                if ( i != j && (a[0] <= b[0] && a[1] >= b[1])) {
                    bool check = true;
                    for(int k = 0; k < points.size(); k++) {
                        if (k==i || k == j) {
                            continue;
                        }
                        vector<int> temp = points[k];
                       
                      if ((a[0] <= temp[0] && temp[0] <= b[0]) && (b[1] <= temp[1] && temp[1] <= a[1])) check = false;
                    }
                    if (check) {
                            ans+=1;
                    }

                   
                }
            }
        }
        return ans;
    }
};