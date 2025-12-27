class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());

        priority_queue<int, vector<int>, greater<int>> free_rooms;

        priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > busy_rooms;

        vector<int> count(n, 0);

        for (int i = 0; i < n; i++) {
            free_rooms.push(i);
        }

        for (auto& meeting : meetings) {
            while (!busy_rooms.empty() && busy_rooms.top().first <= meeting[0]) {
                free_rooms.push(busy_rooms.top().second);
                busy_rooms.pop();
            }

            if (!free_rooms.empty()) {
                busy_rooms.push({meeting[1], free_rooms.top()});
                count[free_rooms.top()]++;
                free_rooms.pop();
            }
            else {
                busy_rooms.push({busy_rooms.top().first + meeting[1] -  meeting[0], busy_rooms.top().second});
                count[busy_rooms.top().second]++;
                busy_rooms.pop();
            }
        }

        

        return max_element(count.begin(), count.end()) - count.begin();

    }
};