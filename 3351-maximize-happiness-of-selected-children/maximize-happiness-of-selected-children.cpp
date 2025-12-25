class Solution {


public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        long long res = 0;
        int selected = 0;

        sort(happiness.begin(), happiness.end(), [](int a, int b) {
            return a > b;
        });


        while (k > 0) {
            int mx = happiness[selected] - selected;
            if (mx > 0) {
                res += mx;
                selected+=1;
            }
            else {
                break;
            }
            k--;
        }

        return res;
    }
};