class Solution {


public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        priority_queue<int> pq;
        long long res = 0;
        int selected = 0;
        for (auto h: happiness) {
            pq.push(h);
        }

        while (k > 0) {
            int mx = pq.top() - selected;
            if (mx > 0) {
                res += mx;
                selected+=1;
                pq.pop();
            }
            else {
                break;
            }
            k--;
        }

        return res;
    }
};