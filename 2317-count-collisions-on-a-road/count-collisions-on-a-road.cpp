class Solution {
public:
    int countCollisions(string directions) {
        int collL = 0;
        int collR = 0;
        int ans = 0;
        for (char d: directions) {
            if (d == 'L') {
                if (collL > 0) {
                    ans+=collL;
                    collL = 1;
                }
                if (collR > 0) {
                    ans+=(collR + 1);
                    collL = 1;
                    collR = 0;
                }
            }
               if (d == 'R') {
                collR += 1;
                collL = 0;
            }

              if (d == 'S') {
                ans += collR;
                collR = 0;
                collL = 1;
            }

      
        }
        return ans;
    }
};