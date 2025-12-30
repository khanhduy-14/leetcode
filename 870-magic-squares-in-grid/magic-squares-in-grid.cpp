class Solution {
public:
    bool check3x3(int r, int c, vector<vector<int>>& grid) {
        int count[10] = {};

        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                if (grid[i][j]>9) return false;
                if (++count[grid[i][j]] > 1) return false;
            }
        }
    
        for (int i = 0; i < 3; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++)
                sum += grid[r + i][c + j];
            if (sum != 15) return false;
        }

 
        for (int j = 0; j < 3; j++) {
            int sum = 0;
            for (int i = 0; i < 3; i++)
                sum += grid[r + i][c + j];
            if (sum != 15) return false;
        }

        if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15) return false;
        if (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15) return false;

         return true;
    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size(), res = 0;
        for (int r = 0; r < row - 2; r++) {
            for (int c = 0; c < col - 2; c++) {
                vector<int> count(10,0); 
                if (check3x3(r, c, grid)) {
                    res+=1;
                }
            }
        }
        return res;
    }
};

