class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<tuple<double,int,int>> q;
        function<double(int, int)> gain = [](int p, int t) {
            return (double)(p + 1) / (t + 1) - (double)p / t;
        };
        double ans  = 0.0;
        for (vector<int> c : classes) {
            ans += (double) c[0] / c[1];
            q.push({gain(c[0], c[1]),c[0], c[1]});
        }

        while(extraStudents--) {
            auto [gr, p, t] = q.top();
            q.pop();
            p++;t++;
            ans += gr;
            q.push({gain(p,t), p, t});
        }
       
    
        return ans / classes.size();
    }
};