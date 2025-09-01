class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<tuple<double,int,int>> q;
        function<double(int, int)> gain = [](int p, int t) {
            return (double)(p + 1) / (t + 1) - (double)p / t;
        };
        for (vector<int> c : classes) {
            q.push({gain(c[0], c[1]),c[0], c[1]});
        }

        while(extraStudents--) {
            auto [gr, p, t] = q.top();
            q.pop();
            p++;t++;
            q.push({gain(p,t), p, t});
        }
        double ans  = 0.0;
        while (!q.empty()) {
            auto [gr, p, t] = q.top();
            q.pop();
            ans+= (double) p / t;
            
        }
        return ans / classes.size();
    }
};