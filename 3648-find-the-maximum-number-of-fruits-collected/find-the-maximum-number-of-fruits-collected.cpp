class Solution {
public:
    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int ans = 0, n= fruits.size();

        for (int i=0; i < fruits.size(); i++){
            ans+=fruits[i][i];
        }
        
        auto dp = [&](auto& self) -> int {
            vector<vector<int>> grid(n, vector<int>(n, 0));
            grid[0][n-1] =  fruits[0][n-1];

            for(int i = 1; i < n - 1; i++) {
                int j = max(i+1, n-1-i);
                for (j; j < n; j++) {
                    int c = max(grid[i-1][j], grid[i-1][j-1]);
                    if (j+1 < n) c = max(c, grid[i-1][j+1]);
                    grid[i][j] = fruits[i][j] + c;
                };
            }

            return grid[n-2][n-1];
        };

        ans+= dp(dp);

        for (int i = 0; i < n;i++) {
            for(int j=0; j<i;j++) {
                swap(fruits[i][j], fruits[j][i]);
            }
        }
        ans+= dp(dp);

        return ans;
        


    }
};