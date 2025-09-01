class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        auto gain = [](int p, int t) {
            return (double)(p + 1) / (t + 1) - (double)p / t;
        };
        
        struct Node {
            double g;
            int p, t;
        };
        
        struct Compare {
            bool operator()(const Node& a, const Node& b) {
                return a.g < b.g; // max-heap
            }
        };
        
        priority_queue<Node, vector<Node>, Compare> pq;
        
        for (auto& c : classes) {
            pq.push({gain(c[0], c[1]), c[0], c[1]});
        }
        
        while (extraStudents--) {
            auto cur = pq.top(); pq.pop();
            int p = cur.p + 1, t = cur.t + 1;
            pq.push({gain(p, t), p, t});
        }
        
        double ans = 0.0;
        while (!pq.empty()) {
            auto cur = pq.top(); pq.pop();
            ans += (double)cur.p / cur.t;
        }
        
        return ans / classes.size();
    }
};
