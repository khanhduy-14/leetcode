class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int ans = 0, s = 0, l = 0, r = 0;

        for (r; r<fruits.size(); r++) {
            s+= fruits[r][1];
            while (l <= r) {
                int c;
                if (startPos < fruits[l][0]) {
                    c = fruits[r][0] - startPos;
                } else if (startPos > fruits[r][0]) {
                    c = startPos - fruits[l][0];
                }
                else {
                    int c1 = (startPos - fruits[l][0]) + (fruits[r][0]-fruits[l][0]);
                    int c2 = (fruits[r][0] -  startPos) + (fruits[r][0]-fruits[l][0]);
                    c = min(c1,c2);
                }

                if (c <= k) {
                    break;
                }
                else {
                    s-= fruits[l][1];
                    l+=1;
                }
            }
            ans = max(ans,s);
        }
        return ans; 
        
    }
};