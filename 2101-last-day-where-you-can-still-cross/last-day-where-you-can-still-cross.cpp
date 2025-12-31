class Solution {
public:
    bool canCross(int day, int row, int col, vector<vector<int>>& cells) {
        vector<vector<int>> grid(row, vector<int>(col, 0));
        for (int i = 0; i < day; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }

        queue<pair<int,int>> q;
        vector<vector<bool>> vis(row, vector<bool>(col, false));

        for (int j = 0; j < col; j++) {
            if (grid[0][j] == 0) {
                q.push({0, j});
                vis[0][j] = true;
            }
        }

        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            if (r == row - 1) return true;

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                    if (!vis[nr][nc] && grid[nr][nc] == 0) {
                        vis[nr][nc] = true;
                        q.push({nr, nc});
                    }
                }
            }
        }
        return false;
    }

    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int left = 0, right = row * col, ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canCross(mid, row, col, cells)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
};
